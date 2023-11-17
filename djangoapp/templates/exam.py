# 1.django orm: it means object Relational mapping
#
# it is used to interact with relational database ina simpler manner it allows to add modify ,delete,a query object
# 2.
# user-->sends request for a resource-->django-->url(checks availability)-->view()-->model__>template
# django follows MvT structure
# M stands for model(it is used to store data in database)
# V stands for view (it is used for handle the web request)
# T stands for template(it contains an html page)
3.
# project :complete configuration
# app: basic logic


# 4.django admin interface:

# one of the prominent role django is the automatic admin interface,it reads metadata from our models to provide an interface
# where the trusted users can manage content on your site
# (it can handle by both buyer and seller)

# 5.context in django:
# context is a variable which help us to pass the  data from backend to frontend
#
#  The context refers is a dictionary of data that is passed from the views to the templates during
#      the process of rendering a web page. This dictionary contains key value pairs where each key represents a variable name,
#      and the corresponding value is the data associated with that variable.

#
# 6.
# Ans: from django.shortcuts import render, redirect, HttpResponse
#      from django.shortcuts import render
#      from django.shortcuts import redirect
#      from django.shortcuts import HttpResponse

7.


# 8.django:it is a free and open-source python based web frame work
# django frontend:django is also a frontend frame which is made of many templates and css,bootstraps are used for its designing
# purpose
# djnago backend:
# it is also a backend frame work .you can store the datas in a datadase by creating model and views

# 10.difference b/w  classbased and functionbased:
# classbased view:
# in classbased view we have to create a form class
# functionbased:it is not necessary to create a form class


# 11. Explain generics and types of generic views ?
# Ans: Generic is a django inbuilt view parent class. They are the advanced det of built inbuilt in views that are used
#      to implement the selective CRUD. Using class based views we can easily handle the get, post request for a view.
#      get() - it is used to retrieve data from a database.
#      post() - it is used to input data into a database field.
#      Classes provided by generic are,
#      1. CreateView - it is a view that is used for creating an intance or object.
#      2. ListView - it is a view that is used to list all instance.
#      3. UpdateView - it is a view that is used for editing an existing object and saving changes.
#      4. DeleteView - it is a view that is used to delete an existing object.
#      5. DetailView - it is a view that is used to get a single instance.

16.
# model

# class ssmodel(models.Model):
#     user_name=models.CharField(max_length=20)
#     email = models.EmailField()
#     dob = models.DateField()
#     password=models.CharField(max_length=20)


# 17.
#
# models.py

# class remodel(models.Model):
#     username = models.CharField(max_length=30)
#     email = models.EmailField()
#     password = models.CharField(max_length=30)

# forms.py

# class reg_form(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = remodel
#         fields = ['username', 'email', 'password']

# views.py

# class reg_view(CreateView):
#     template_name = 'reg.html'
#     form_class = reg_form
#     success_url = reverse_lazy('login')

# html

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>User Registration</title>
# </head>
# <body>
#     <h2>User Registration</h2>
#     <form method="post">{% csrf_token %}
#         {{ form.as_p }}
#         <button type="submit">Register</button>
#     </form>
# </body>
# </html>

# url.py

# urlpatterns = [
#     path('register/', reg_view.as_view(), name='reg'),
# ]


# 18.the package that we install to connect django ang mysql is pip: python installer package
# pip install django
# django-admin startproject projectname
# cd projectname
# python manage.py startapp appname
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver

# 12.meta class: metaclass in python is a class of a class that defines how a class behaves
#
# 14.
#  In Django, request.session is a dictionary-like object that allows you to store and retrieve arbitrary
#      data on a per-site-visitor basis. This allows us to maintain state and user-specific information across multiple
#      requests from the same user.
# 15.get and post
# get:it is used to retrieve data drom database
# post:it is used to input a data into database field  register,login using post
# get queryset:which is used by listview it determines the list of objects that you want to display


# 9.type error:
# it is raised when an operation  or function is applied to an object of the wrong type
# name error:
# it is raised when a variable or a function name is not found in the currentscope