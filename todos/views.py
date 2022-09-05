from glob import escape
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from todos.models import Collection

from todos.models import Task


def index(request):

    col_slug=request.GET.get("collection")
    if col_slug:
        collection=get_object_or_404(Collection,slug=col_slug)
    else:
        collection=Collection.default_collection()

    collections=Collection.objects.order_by("slug")
    tasks=collection.task_set.order_by("description")
    return render(request,"todos/index.html",context={"collections":collections,"tasks":tasks})

def add_collection(request):
    collection_name=request.POST.get('collection-name')

    print(collection_name)
    collection,created=Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("La collection existe déja",status=409)

    return HttpResponse(f"<h2>{collection_name}</h2>")

def add_task(request):
    collection=Collection.default_collection()
    descripton=request.POST.get('task-desc')
    Task.objects.create(description=descripton,collection=collection)

    return HttpResponse(f"<h2>{descripton}</h2>")

def get_tasks(request,col_pk):
    collection=get_object_or_404(Collection,pk=col_pk)
    tasks=collection.task_set.order_by("description")
    return render(request,"tasks.html",context={"tasks":tasks})