import email
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout as emp_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.db.models import F
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.db.models import Q
from .models import *
import random

# Create your views here.
def index(request):
    if request.method == "POST":
        # employee_id = request.POST['employee_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        job_role = request.POST['job_role']
        salary = request.POST['salary']

        user_exist_check = Employee.objects.filter(Q(first_name=first_name) & Q(last_name=last_name)).exists()

        if not user_exist_check:
            new_employee = Employee.objects.create(first_name=first_name, last_name=last_name, email=email, job_role=job_role, salary=salary)
            new_employee.save()
            return redirect('/login/')
        else:
            messages.warning(request, "User Alredy Exist")
            return redirect('home')

    else:
        return render(request, 'crud_app/index.html')


def show(request):
    if login_check(request):
        employee_data = Employee.objects.all()
        employee_data_count = Employee.objects.count()
        employee_data_lst = []
        
        for data, serial_no in zip(employee_data, range(1,employee_data_count+1)):
            employee_data_lst.append({
                'serial_no':serial_no,
                'employee_id': data.employee_id,
                'first_name':data.first_name,
                'last_name':data.last_name,
                'job_role':data.job_role,
                'salary':data.salary
            })
        
        # print(employee_data_lst)
            

        first_name = request.session['first_name']
        last_name = request.session['last_name']

        profile_name = f"{first_name} {last_name}"

        return render(request, 'crud_app/show_data.html',{
            "employee_data": employee_data_lst,
            "profile_name": profile_name
        })

    else:
        return redirect('login')

def delete_data(request, emp_id):
    delete_employee = Employee.objects.get(employee_id=emp_id)
    delete_employee.delete()

    # count = Employee.objects.count()
    # update_id_test = Employee.objects.all().filter(employee_id=emp_id)[1:]
    # print(update_id_test)

    # update_id = Employee.objects.all()
    # if count > 1:
    #     update_id.update(employee_id=F('employee_id') - 1)
    return redirect('/show/')


def edit_data(request, emp_id):
    if request.method == "POST":
        employee_record = Employee.objects.get(employee_id=emp_id)
        employee_record.first_name = request.POST['first_name']
        employee_record.last_name = request.POST['last_name']  
        employee_record.job_role = request.POST['job_role']
        employee_record.salary = request.POST['salary']
        employee_record.save()

        return redirect('show')

    else:
        employee_record = Employee.objects.get(employee_id=emp_id)
        return render(request, 'crud_app/update.html', {
            "employee": employee_record
        })  


def login_view(request):
    if request.method == "POST":
        user_email = request.POST['email']
        try:
            employee_login = Employee.objects.get(email=user_email)
            first_name = employee_login.first_name
            last_name = employee_login.last_name

            if employee_login:
                otp_genrate = random.randint(1111,9999)

                subject = 'OTP Verification'
                message = f"Your Otp Is: {otp_genrate}"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user_email]
                send_mail( subject, message, email_from, recipient_list )
                
                request.session['user_email'] = user_email
                request.session['otp_email'] = otp_genrate
                request.session['first_name'] = first_name
                request.session['last_name'] = last_name

                return redirect('otp_verify')
        except:
            messages.info(request, "Invalid Email")
            return redirect('login')

    return render(request, 'crud_app/login.html')

    
    # if request.method == "POST":    
    #     employee_id = request.POST['email']
    #     job_role = request.POST['job_role']

    #     employee_login = Employee.objects.filter(Q(employee_id=employee_id) & Q(job_role=job_role)).exists()

    #     if employee_login:
    #         request.session['employee_id'] = employee_id    
    #         return redirect('show')
    #     else:
    #         messages.error(request, 'Enter Valid Authentication')
    #         return redirect('login')
    
    # return render(request, 'crud_app/login.html')


def logout_view(request):
    try:
        del request.session['user_email']
        del request.session['otp_email']
        del request.session['first_name']
        del request.session['last_name']
    except:
        print("Delete session error")
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def login_check(request):
    try:
        if request.session['user_email']:
            return True
        else:   
            return False
    except:
        return False

def otp_verify(request):
    if request.method == "POST":    
        otp_email = request.POST['otp_email']
        otp_session = request.session['otp_email']
        if otp_session == int(otp_email):
            return redirect('show')
        
    return render(request, 'crud_app/email_otp.html')   
