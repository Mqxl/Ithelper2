from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from django.http import HttpResponse
# Create your views here.


def index(request):
    
    
    projects = Project.objects.all()
    pricing = Pricing.objects.all()
    reviews = Reviews.objects.filter(available = True)
    
 
    

    form = Reviewsform(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,'return.html')
         
    if request.method == 'POST':
        if request.POST.get('email')  and request.POST.get('question') :
            post=Question()
            post.email= request.POST.get('email')
            post.questiontext = request.POST.get('question')
            post.save()
            return render(request,'return.html')
 
    return render(request,'index.html',{'projects':projects,'pricing':pricing,'reviews':reviews,'form':form} )   
   
def project_detail(request, id):
    projects = get_object_or_404(Project,id=id)
    
    image_list = projects.images.all()
    
    
    return render(request, 'detail.html', {'projects': projects,'image_list':image_list})