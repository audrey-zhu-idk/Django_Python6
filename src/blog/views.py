from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blog_post_detail_page(request):
    data = BlogPost.objects.get(id=1)
    context = {"object":data}
    return render(request,"blog_post_detail.html", context)