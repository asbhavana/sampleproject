from django.test import render

# Create your tests here.
def home(request):
    return render(request,'base.html')