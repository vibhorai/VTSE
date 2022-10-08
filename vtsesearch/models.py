from django.db import models
from .search import BGIndex

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])

class VedicText(models.Model):
     title = models.CharField(max_length=500)
     translation = models.CharField(max_length=5000)
     url=models.CharField(max_length=5000)

     def indexing(self):
        obj = BGIndex(
            meta={'id': self.id},
            title=self.title,
            url=self.url,
            translation=self.translation
        )
        obj.save()
        return obj.to_dict(include_meta=True)