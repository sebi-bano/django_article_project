from django.shortcuts import render
from .models import article
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.


def at_article(request):
  if request.method=='GET':
    return render(request,"home.html")

  if request.method=='POST':
    # title_name = request.POST['title']
    data = request.POST
    # article_obj = article.objects.create(title=data['title'])
    
    user = User.objects.get(id=int(data['created']))
    article_obj = article(title=data['title'],created_by=user,description=data['description'],Creation_date=data['date'],Is_published=bool(data['published']) )
    
    article_obj.save()
    
    return JsonResponse({"success": "Sucessfully submitted."})

