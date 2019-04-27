from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PG_selection(models.Model):
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return self.name

class Help_and_Support(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_no =  models.CharField(max_length=10)
    PG_selection = models.ForeignKey(PG_selection, on_delete=models.CASCADE)
    comments_on_PG = models.TextField()
    comments_on_website = models.TextField()
    satisfied = models.BooleanField()
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.customer_name

class Cust_Signup(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
   
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2', )

        def __str__(self):
          return self.username

class Landdetails(models.Model):
    retype_username = models.CharField(max_length=250)
    retype_email =  models.EmailField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    Hostel_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    Female_or_Male = models.CharField(max_length=50)
    Mess =  models.CharField(max_length=50, default='')
    Pictures = models.CharField(max_length=1000)
    Rent = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
   
    def __str__(self):
          return self.Hostel_name

class Designation(models.Model):
    name =  models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Custdetails(models.Model):
    retype_username = models.CharField(max_length=250)
    retype_email =  models.EmailField()
    Phone_no =  models.CharField(max_length=10)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    Date_of_Birth = models.DateField(null=True, blank=True)
    Female_or_Male = models.CharField(max_length=50)
    Designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    Address = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
   
        
    def __str__(self):
        return self.retype_username + ' - ' + self.first_name 






