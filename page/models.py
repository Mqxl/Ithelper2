from django.db import models

# Create your models here.
class Project(models.Model):
    projectname = models.CharField(max_length=200, db_index=True)
    projectdescription = models.TextField()
    projectmaintext = models.CharField(max_length=200, db_index=True)
    projectsecondtext = models.CharField(max_length=200, db_index=True)
    

    def __str__(self):
        return self.projectname

class ProjectImage(models.Model):
    property = models.ForeignKey(Project, related_name='images' ,on_delete=models.CASCADE)
    image = models.ImageField()

class Pricing(models.Model):
    cardtitle = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    pricingfirst = models.CharField(max_length=200, db_index=True)
    pricingsecond = models.CharField(max_length=200, db_index=True,null=True)
    pricingthird = models.CharField(max_length=200, db_index=True,null=True)
    pricingfour = models.CharField(max_length=200, db_index=True,null=True)
    pricingfive = models.CharField(max_length=200, db_index=True,null=True)
    def __str__(self):
        return self.cardtitle


class Reviews(models.Model):
    reviewsname = models.CharField(max_length=200, db_index=True)
    reviewstext = models.CharField(max_length=400, db_index=True)
    reviewsinstagram = models.CharField(max_length=400, db_index=True)
    
    available = models.BooleanField(default=False)
