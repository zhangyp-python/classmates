from django.db import models

# Create your models here.
class ClassMates(models.Model):
    name=models.CharField(max_length=20)
    t_n1=models.CharField(max_length=200,null=True)
    t_n2=models.CharField(max_length=200,null=True)
class Mates_node(models.Model):
    node=models.CharField(max_length=200)
    node_time=models.DateTimeField(auto_now_add=True)
    mate_node=models.ForeignKey(to=ClassMates,on_delete=models.CASCADE)
