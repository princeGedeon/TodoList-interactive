from django.urls import path

from todos.views import index

from todos import views

urlpatterns = [
    path('', index,name="home"),
    path('add_collection',views.add_collection,name="add_collection"),
    path('add_task/',views.add_task,name="add_task")

]
