# Model Videw emplate (MVT)
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# one web view is one function in this views.py file
def home_page(request):
    my_title = "My Home Page"
#     return HttpResponse("<h1>My Home Page</h1>")
    return render(request,"home_page.html",{"h1":my_title}, "title":"HOME", "button_text":"Home Button") 
    # I want to replace the "title" in curly brackets to the variable my_title
    # Second parameter replacement for "title" replaces the tab name (the name that you see beside the icon)

def about_page(request):
#     return HttpResponse("<h1>Welcome to About Page</h1>")
    return render(request,"about_page.html",{"h1":"About us"}, "title":"ABOUT")
    # "h1" means a variable- looking for that title name that defines tab name in home_page.html

def contact_page(request):
#     return HttpResponse("<h1>Contact us</h1>")
    return render(request,"contact_page.html",{"h1":"Contact us"}, "title":"CONTACT")

def example(request):
    # the code below is the same thing as doing: return render(request,"contact_page.html",{"h1":"Contact us"}, "title":"CONTACT")
    # context = {"h1":"Example"}
    # template_name = "Strings-Example.txt"
    # rendered_strings = get_template(template_name).render(context)
    # return HttpResponse(rendered_item)
    return render(request,"home_page.html",{"h1":"Example"}, "title":"HOME")

def project_page(request):
    return render(request,"project_page.html",{"h1":"Project Intro"}, "title":"INTRO")