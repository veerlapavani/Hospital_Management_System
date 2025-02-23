from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('departments/', views.department_list, name='department_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('profile/', views.patient_profile, name='patient_profile'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
]

