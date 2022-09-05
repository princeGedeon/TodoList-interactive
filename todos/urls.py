from django.urls import path

from todos.views import index

urlpatterns = [
    path('', index,name="index"),

]
