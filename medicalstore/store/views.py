from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import SignupForm,MedicineForm
from .models import Medicine



def home(request):
    return render(request,'home.html')



def signup_view(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('list')
        else:
            messages.error(request,"Invalid credentials")
    return render(request,'login.html')

@login_required
def add_medicine(request):
    count = Medicine.objects.filter(user=request.user).count()
    if count >= 5:
        messages.error(request,"You can add only 5 medicines")
        return redirect('list')
    form = MedicineForm()
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            return redirect('list')
    return render(request,'add.html',{'form':form})

@login_required
def list_medicines(request):
    search = request.GET.get('search','')
    medicines = Medicine.objects.filter(user=request.user)
    if search:
        medicines = medicines.filter(name__icontains=search)
    paginator = Paginator(medicines,5)
    page = request.GET.get('page')
    medicines = paginator.get_page(page)
    return render(request,'list.html',{'medicines':medicines})

@login_required
def edit_medicine(request,id):
    medicine = get_object_or_404(Medicine,id=id,user=request.user)
    form = MedicineForm(instance=medicine)
    if request.method == "POST":
        form = MedicineForm(request.POST,instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request,'edit.html',{'form':form})

@login_required
def delete_medicine(request,id):
    medicine = get_object_or_404(Medicine,id=id,user=request.user)
    medicine.delete()
    return redirect('list')

def logout_view(request):
    logout(request)
    return redirect('login')






