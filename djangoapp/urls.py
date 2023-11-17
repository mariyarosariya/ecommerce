#app...>create a python file urls.py
from django.urls import path
from .views import *
# urlpatterns=[
#     path('first/',first)
# ]
# urlpatterns=[
#     path('second/',second)
# ]
# # render:is a function that is used to connect your function with templates to return a user interface layer
#
#
# urlpatterns=[
#     path('third/',third)
# #  ]
# urlpatterns=[
#     path('name/',fourth)
# # ]
# cd djangopro
#
# urlpatterns=[
#     path('index/',index),
# ]
# urlpatterns=[
#     path('reg/',fun5),
#     path('log',funlog),
#     path('ind',funind),
#
# ]
# urlpatterns=[
#     path('employee/',employee)
#
# ]

# urlpatterns=[
path('login/',login),
#
# ]
# urlpatterns=[
#     path('product/',product)
# ]
# urlpatterns=[
#     path('filem/',funupload)
# ]
# #
# urlpatterns=[
#     path('search',regmodel1)
#
# ]
# urlpatterns=[
#     path('regi/',regi)
# ]
# urlpatterns=[
#     path('regis',funreg),
#
#     path('display',display),
#     path('file',filedisplay),
#     path('updatedata/<int:id>',update_data),
#
#
#
# ]
# in the case of number checking we have to use int
# #work
# create an html file
# audio name

# video name
# video
# pdf name
# pdf

# image,imagename,description
urlpatterns=[
    path('regi/',regi),
    path('filem/',funupload),
    path('employee/', employee),
    path('login/',login),
    path('audio',audios),#(urls,function name)
    path('pdf',filedisplay),
    path('fileup/',funupload),
    path('imagedisp/',imagedisplay1),
    path('edit/<int:id>',fileedit),
    path('ammu/',audioedisplay),
    path('delete/<int:id>',vaccanydelete),
    path('authuserreg/',userregisteration),
    path('userlog/',custom_login),
    path ('register/',reg1.as_view(),name='register'),
    path('login1/',loginn.as_view(),name='login'),
    path('disp/',UserListView.as_view(),name='disp'),
    path('register1/',userregistration.as_view(),name='register1'), #doubt
    # path('login3/',uselog.as_view(),name='login3'),  #doubt
    path('del/<pk>',re.as_view(),name='del'),#     pk: primary key
    path('detail/<pk>',detail.as_view(),name='detail'),
    path('up/<pk>',up.as_view(),name='up'),
    path('register1/',registerauth.as_view(),name='register1'),
    path('authlogin/', authuser.as_view(),name='authlogin'),
    path('fileupload/', fileclass.as_view(),name='fileupload'),
    path('filedisplay/', Filedisp.as_view(),name='filedisplay'),
    path('movie/',movie_passing.as_view()),
    path('api/',api_view.as_view())






]
