from django.shortcuts import render
from .models import PostProject

# Create your views here.
def project_post_detail_page(request):
    data = PostProject.objects.get(id=1)
    descr_one = {"object":data}
    return render(request,"project_post_detail.html", descr_one)