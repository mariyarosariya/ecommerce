from django import forms
from django.contrib.auth.models import User
from .models import*

class userreg(forms.Form):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

#       what is Meta class
# class META :meta class is usally the the inner class which is basically used to provide meta data to the model form or the model
# class
#     it is used to change the behaviour of your exisiting form



class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    conf=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','conf']


# superadmin:staff status true
# admin:User model

class userlogin(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)

class regform(forms.ModelForm):
    class Meta:
        model=Smodels
        fields='__all__' #['name','email','password']


class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)




# class userreg(forms.ModelForm):
#
#     class Meta:
#         model=User
#         fields=['username','first_name','last_name','email','password']
#
# class logform1(forms.Form):
#     email=forms.CharField(max_length=50)
#     password=forms.CharField(max_length=50)

class userreg(forms.ModelForm):
    confirm=forms.CharField(max_length=20,widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm']

class authlogin(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)

class fileform(forms.ModelForm) :
    class Meta:
        model=filemodel
        fields='__all__'