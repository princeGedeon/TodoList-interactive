from django.db import models

# Create your models here.
from django.utils.text import slugify


class Collection(models.Model):
    name=models.CharField(max_length=60)
    slug=models.SlugField(blank=True)

    @classmethod
    def default_collection(cls):
        collection,_=cls.objects.get_or_create(name="Default",slug="_default")
        return collection

    def __str__(self) -> str:
        return self.name

    def save(self,*args,**kwargs):
        self.slug=self.slug or slugify(self.name)

class Task(models.Model):
    description=models.CharField(max_length=300)
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE)

