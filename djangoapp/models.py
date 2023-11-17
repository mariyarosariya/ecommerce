from django.db import models

# Create your models here.
# fname,lname,username,email,phone,gender,address,dob,password,cpass
class register(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    dob=models.DateField()
    password=models.CharField(max_length=20)

    
# class fileupld(models.Model):
#     fname=models.CharField(max_length=50)
#     fimage=models.ImageField
#     fdescription=models.CharField(max_length=50)
class employee(models.Model):
    empname=models.CharField(max_length=30)
    email=models.EmailField()
    company=models.CharField(max_length=20)
    desig=models.CharField(max_length=20)
    phone=models.IntegerField

# class product(models.Model):
#     pname=models.CharField(max_length=100)
#     price=models.IntegerField()
#     brand=models.CharField(max_length=100)
#     quantity=models.IntegerField()
#     exp=models.DateField()
#     des=models.CharField(max_length=100)

class fileupload(models.Model):
    fname=models.CharField(max_length=20)
    fileimage=models.FileField(upload_to='djangoapp/static')
    description=models.CharField(max_length=200)

class file1(models.Model):
    audio=models.CharField(max_length=20)
    audio1=models.FileField(upload_to='djangoapp/static')
    video=models.CharField(max_length=20)
    video1=models.FileField(upload_to='djangoapp/static')
    pdf=models.CharField(max_length=20)
    pdf1=models.FileField(upload_to='djangoapp/static')
# class fil2(models.Model):
#     audio = models.CharField(max_length=20)
#     audio1=models.FileField(upload_to='djangoapp/static')
#     video=models.CharField(max_length=20)
#     video1=models.FileField(upload_to='djangoapp/static')
#     pdf=models.CharField(max_length=20)
#     pdf1=models.FileField(upload_to='djangoapp/static')

# class regmodel1(models.Model):
#     choice=[
#         ('kerala','kerala'),#(database,label(template))
#         ('tamil nadu','tamil nadu'),
#         ('karnataka','karnataka')
#
#     ]
#
#
# name=models.CharField(max_length=30)
# state=models.CharField(max_length=30,choices=choice)
# english=models.BooleanField(default=False)
# malayalam=models.BooleanField(default=False)
# hindi=models.BooleanField(default=False)

class regmodel1(models.Model):
    #select
    choice=[
        ('kerala','kerala'),  #database,label(template
        ('karnataka','karnataka'),
        ('goa','goa')
    ]
    name=models.CharField(max_length=30)
    state=models.CharField(max_length=30,choices=choice)#select
    #checkbox
    english=models.BooleanField(default=False)
    malayalam = models.BooleanField(default=False)
    hindi = models.BooleanField(default=False)




class regmodel(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    dob=models.DateField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


class Smodels(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class filemodel(models.Model):
    itemname=models.CharField(max_length=20)
    image=models.FileField(upload_to='media')
