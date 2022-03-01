from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import teams


# Create your views here.
def demo(request):
   obj=place.objects.all()
   obj1=teams.objects.all()
   return render(request,'index.html',{'result':obj,'result1':obj1})
# def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    result=x+y
#    return render(request,'result.html',{'sum':result})

# def about(request):
#    return render(request,'about.html')
# def contact(request):
#    return HttpResponse('python learner')