from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from .models import UserModel
from .forms import HospitalForm
from datetime import *

def home(request) :
	dt = datetime.now()
	return render(request , "home.html" , {"data" : dt} )

def main(request) :
	if request.method == 'POST':
		user_type = request.POST.get('hos')  # Get the value of the selected radio button
		if user_type == 'pat':
			return redirect('patient_dashboard')  # Redirect to patient dashboard
		elif user_type == 'doc':
			return redirect('ulogin')  # Redirect to doctor dashboard
    
	return render(request , "main.html")

def doctor_dashboard(request) :
	if request.user.is_authenticated : 
		data = UserModel.objects.all()
		return render(request , "doctor_dashboard.html", {"data" : data})
	else :
		return redirect("ulogin")
	

def patient_dashboard(request) :
	if request.method == "POST" :
		data = HospitalForm(request.POST , request.FILES)
		if data.is_valid():
				data.save()
				msg = "Registeration Completed"
				fm = HospitalForm()
				return render(request , "patient_dashboard.html", {"fm": fm, "msg": msg})
		else :
				msg = "Check Errors"
				fm = HospitalForm()
				return render(request , "patient_dashboard.html", {"fm": fm, "msg": msg})
	else :
			fm = HospitalForm()
			return render(request , "patient_dashboard.html", {"fm": fm})



# Create your views here.

def ucp(request):
	if request.user.is_authenticated : 
		if request.method == "POST" :
			pw1 = request.POST.get("pw1")
			pw2 = request.POST.get("pw2")	
			if pw1 == pw2 :
				usr = User.objects.get(username = request.user.username)
				usr.set_password(pw1)
				usr.save()
				logout(request)
				return redirect("ulogin")
			else :
				msg = "Password did not match"
				return render(request , "ucp.html" , {"msg" : msg})
		else :
			return render(request , "ucp.html")
	else :
		return redirect("ulogin")



def usignup(request) :
	if request.user.is_authenticated : 
		return redirect("doctor_dashboard")
	else :
		if request.method == "POST" :
			un = request.POST.get("un")
			pw1 = request.POST.get("pw1") 
			pw2 = request.POST.get("pw2")
			if pw1 == pw2 :
				try :
					usr = User.objects.get(username = un)
					msg = "User Already Exists"
					return render(request , "usignup.html" , {"msg" : msg})


				except User.DoesNotExist :
					usr = User.objects.create_user(username= un , password = pw1)
					usr.save()
					return redirect("ulogin")

			else :
				msg = "Invalid Username/ Password"
				return render(request , "usignup.html" , {"msg" : msg})
		
		else :
			return render(request , "usignup.html")


def ulogin(request) :	
	if request.user.is_authenticated :
		return redirect("doctor_dashboard")

	else :	
		if request.method == "POST" :
			un = request.POST.get("un")
			pw = request.POST.get("pw")
			usr = authenticate(username = un , password = pw)
			if usr is None :
				msg = "Check username/password"
				return render(request , "ulogin.html" , {"msg" : msg})

			else :
				login(request , usr)
				return redirect("doctor_dashboard")

		else :
			return render(request , "ulogin.html")



def ulogout(request) :
	logout(request)
	return redirect("ulogin")


def remp(request , id):
	dt=UserModel.objects.get(patient_id=id)
	dt.delete()
	return redirect("doctor_dashboard")


	