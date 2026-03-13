from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from django.shortcuts import get_object_or_404, redirect
from .models import User
# Create your views here.

#this function will add new item and show all items

def add_show(req):
    if req.method == 'POST':
        fm = StudentRegistration(req.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(req, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

#this function will update/edit
def update_data(req, id):
    pi = get_object_or_404(User, pk=id)  # get user or 404
    
    if req.method == 'POST':
        fm = StudentRegistration(req.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')  # redirect after successful POST to avoid resubmission
    else:
        fm = StudentRegistration(instance=pi)  # GET request: pre-fill form with existing data
    
    return render(req, 'enroll/updatestudent.html', {'form': fm})



#ths function will delete
def delete_data(req, id):
    if req.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')







