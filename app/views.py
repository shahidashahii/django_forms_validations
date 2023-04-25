from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def student(request):
    SFO=Student_Form()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=Student_Form(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))


    return render(request,'student.html',d)