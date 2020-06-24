from django.db import models

# Create your models here.

class Organisarion(models.Model):
   
    org_name = models.CharField(max_length=250)
    

    def __str__(self):
        return self.org_name

class Branch(models.Model):
    
    branch_name = models.CharField(max_length=250)
    address = models.TextField()
    org = models.ForeignKey(Organisarion,on_delete=models.CASCADE,related_name="orgs", blank=True, null=True)

    def __str__(self):
        return f"{self.branch_name}"