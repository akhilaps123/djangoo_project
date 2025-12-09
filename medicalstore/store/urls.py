from django.urls import path
from .import views

urlpatterns = [
    path('signup',views.signup_view,name='signup'),
    path('',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('add/',views.add_medicine,name='add'),
    path('list/',views.list_medicines,name='list'),
    path('edit/<int:id>/',views.edit_medicine,name='edit'),
    path('delete/<int:id>/',views.delete_medicine,name='delete')
]