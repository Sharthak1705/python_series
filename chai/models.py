from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ChaiVarity(models.Model):
    CHOICE = [
        {'ML', 'Masala'},
        {'DL', 'Doodh'},
        {'GL', 'Ginger'},
        {'EL', 'Elaichi'},
        {'KL', 'KIWI'},
        {'LA', 'lattice'},
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='chais/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=7, choices=CHOICE) 
    description = models.TextField(default='')
    def __str__(self):
       return self.name
    
# one to many

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
    #many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length = 100)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name= 'stores')

    def __str__(self):
        return self.name
    
#one to one
 
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, related_name='certificate', on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length= 100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai}'
