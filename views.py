from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, AppointmentForm
from .models import Doctor, Appointment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Department, Doctor, Patient, Appointment
from .forms import AppointmentForm

# Home Page
def home(request):
    return render(request, 'home.html')

# Register View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')

# Appointment Booking View
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.status = 'Pending'
            appointment.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

# Assuming you create an AppointmentForm in forms.py

# Department List View
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hospital/departments.html', {'departments': departments})

# Doctor List View
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctors.html', {'doctors': doctors})

# Doctor Detail View
def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'hospital/doctor_detail.html', {'doctor': doctor})

# Patient Profile View
@login_required
def patient_profile(request):
    patient = get_object_or_404(Patient, user=request.user)
    return render(request, 'hospital/patient_profile.html', {'patient': patient})

# Appointment Booking View
@login_required
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = get_object_or_404(Patient, user=request.user)
            appointment.status = 'Pending'
            appointment.save()
            return redirect('appointment_list')  # Redirect to the appointment list page
    else:
        form = AppointmentForm()
    return render(request, 'hospital/book_appointment.html', {'form': form})

# Appointment List View
@login_required
def appointment_list(request):
    patient = get_object_or_404(Patient, user=request.user)
    appointments = Appointment.objects.filter(patient=patient).order_by('-date')
    return render(request, 'hospital/appointments.html', {'appointments': appointments})

