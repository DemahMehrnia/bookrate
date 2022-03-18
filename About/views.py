from django.shortcuts import render

# Create your views here.
def About_page(request):
    return  render(request, 'About/about.html')

def About_Booka(request):
    return  render(request, 'About/aboutbooka.html')

def bookazerotohundred(request):
    return  render(request, 'About/bookaztoh.html')

def help(request):
    return render(request,'About/help.html')