from django.db import models
from datetime import date
class Todo(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    descripcion=models.TextField(max_length=100,blank=True,null=True)
    date=models.DateField(default=date.today)
    estimated_end=models.DateTimeField(blank=True,null=True)
    priority=models.IntegerField(default=3)
    
    def __str__(self):
        return self.title
 
 