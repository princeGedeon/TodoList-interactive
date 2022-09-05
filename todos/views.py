from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from todos.models import Collection


def index(request):
    collection=Collection.default_collection
    collections=Collection.objects.order_by("name")
    return render(request,"todos/index.html",context={"collections":collections})

def add_collection(request):
    collection_name=request.POST.get('collection-name')

    print(collection_name)
    collection,created=Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("La collection existe déja",status=409)

    return HttpResponse(f"<h2>{collection_name}</h2>")

    