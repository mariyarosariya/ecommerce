from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login
from django.views import generic
from django.urls import reverse_lazy
import json
from rest_framework.views import APIView


# HttpResponse: it is used in django to get a text response in our webpage

# Create your views here.
# def first(request):
#     return HttpResponse("my first django page")
# second
# def second(request):
#     return HttpResponse("my second django page")
# def third(request):
#     return render(request,'third.html')
# work:
# maintopic,center,underline
# paragraph

def fourth(request):
    return render(request,'fourth.html')
def regi(request):#request=request.html
    if request.method=='POST':

        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        username=request.POST.get('username')
        mail=request.POST.get('email')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        password=request.POST.get('password')
        copassword=request.POST.get('cpassword')
        if password==copassword:
            a=register(fname=firstname,lname=lastname,username=username,email=mail,phone=phone, gender=gender,dob=dob,address=address,password=password)
            a.save()
            return HttpResponse("registration success")
        else:
            return HttpResponse("password incorrect")

    return render(request,'regi.html')
# def index(request):
#     return render(request,'index.html')

# django  orm that stands for object relational mapping
# it is used to interact with relational database ina simpler manner it allows to add modify ,delete,a query object
def funupload(request):
     if request.method=='POST':
          flnm=request.POST.get('filename')
          image=request.FILES.get('fileimage')
          desc=request.POST.get('description')
          b=fileupload(fname=flnm,fileimage=image,description=desc)
          b.save()
          return HttpResponse("fileupload success")


     return render(request,'fileupload.html')

# what is csrf ;it stands for cross site request forgery
# its a attack that forces authenticated users to submit a request to a web application for avoiding that we passes a token into
# our html file
# employee register page
# empolyee name,email,companyname.designation,phone
# def emloyee(request):
def employee(request):
    if request.method =='POST':

            emp_name=request.POST.get('emp_name')
            email=request.POST.get('email')
            company=request.POST.get('com')
            desig=request.POST.get('desi')
            phone=request.POST.get('pho')
            a=employee(empname=emp_name,email=email,com=company,desi=desig,pho=phone)
            a.save()
            return HttpResponse("registration success")
    return render(request,'employee.html')


# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
      #   a=register.objects.all()
      #   for i in a:
      #       if (i.email==email and i.password==password):
      #           return HttpResponse("login successfull")
      #   else:
      #       return HttpResponse("login failed")
      #
      # return  render(request,'login.html')
    # model_name.object.all():it is a an orm query that is used to fetch a table in our model field
#     create an html page with fields :
# product details:
# productname,price,product company name,quantity,expirary dates
# def product_details(request):
#     if request.method=='POST':
#          pname=request.POST.get('pname')
#          price=request.POST.get('price')
#          brand=request.POST.get('brand')
#          qty=request.POST.get('quan')
#          exp=request.POST.get('ex')
#          des =request.POST.get('des')
#          v=product(pname=pname,price=price,brand=brand,quan=qty,ex=exp,des=des)
#          v.save()
#          return HttpResponse('product added successfully')
#
#     return render(request,'product.html')
#

# def fileup(request):
#     if request.method=='POST':
#         fname=request.POST.get('filename')
#         image=request.FILES.get('fileimage')
#         description=request.POST.get('description')
#         a=fileupload(fname=fname,fileimage=image,description=description)
#         a.save()
#         return HttpResponse('fileupload success')
#
#     return render(request,'fileupload.html')


def audios(request):
    if request.method=='POST':
        audio=request.POST.get('audioname')
        audio1=request.FILES.get('fileaudio')
        video=request.POST.get('videoname')
        video1=request.FILES.get('filevideo')
        pdf=request.POST.get('pdfname')
        pdf1=request.FILES.get('filepdf')
        b=file1(audio=audio,audio1=audio1,video=video,video1=video1,pdf=pdf,pdf1=pdf1)
        b.save()
        return  HttpResponse("success")
    return  render(request,'audio.html')
# def vid(request):
#     if request.method == 'POST':
#         audio=request.POST.get('audioname')
#         audio1=request.FILES.get('fileaudio')
#         video=request.POST.get('videoname')
#         video1=request.FILES.get('filevideo')
#         pdf=request.POST.get('pdfname')
#         pdf1=request.FILES.get('filepdf')
#         a=fil2(audio=audio,audio1=audio1,video=video,video1=video1,pdf=pdf,pdf1=pdf1)
#         a.save()
#         return HttpResponse("success")
#     return  render(request,'work.html')








# def funselect(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         state=request.POST.get('state')
#         english=request.POST.get('english')
#
#         if english=='on':
#             english=True
#         else:
#             english=False
#         malayalam = request.POST.get('malayalam')
#         if malayalam=='on':
#             malayalam=True
#         else:
#             malayalam=False
#         hindi = request.POST.get('hindi')
#         if hindi=='on':
#             hindi=True
#         else:
#             hindi=False
#
#         gg=regmodel1(name=name,state=state,english=english,malayalam=malayalam,hindi=hindi)
#         gg.save()
#         return HttpResponse('success......')
#     return render(request,'search.html')

def display(request):
    a=register.objects.all()
    return render(request,'display.html',{'data':a})
# context:is a  dictionary in jango which is used to pass  your datas from backend to frontend
def funreg(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            aa=regmodel(fname=fname,lname=lname,email=email,phone=phone,gender=gender,address=address,dob=dob,username=username,password=password)
            aa.save()
            return HttpResponse('registeration success')
        else:
            return HttpResponse('password incorrect')
    return render(request,'regi.html')

# doubt in model name(206 line)
def display(request,id):
    ab=regmodel.objects.all()
    return render(request,'regdisplay.html',{'data':ab})
def imagedisplay1(request):
    id=[]
    name=[]
    im=[]
    des=[]
    aa=fileupload.objects.all()
    for i in aa:
        id1=i.id
        id.append(id1)
        name1=i.fname
        name.append(name1)
        image1=str(i.fileimage).split('/')[-1]
        im.append(image1)
        des1=i.description
        des.append(des1)
    mylist=zip(id,name,im,des)
    return render(request,'imgupload.html',{'data':mylist})


def fileedit(request,id):
    cc=fileupload.objects.get(id=id)
    if request.method=='POST':
        cc.fname=request.POST.get('filename')
        cc.fileimage=request.FILES['fileimage']
        cc.description=request.POST.get('description')
        cc.save()
        return redirect(imagedisplay1)

    return render(request,'imgedit.html',{'data':cc})




def filedisplay(request):
    id=[]  #variable name is not same as list
    audioname=[]
    aud=[]
    videoname=[]
    vid=[]
    filename=[]
    fil=[]
    bb=file1.objects.all()
    for i in bb:
        id1=i.id
        id.append(id1)
        audnm=i.audio
        audioname.append(audnm)
        aud1=str(i.audio1).split('/')[-1]
        aud.append(aud1)
        vidnm=i.video
        videoname.append(vidnm)
        vid1=str(i.video1).split('/')[-1]
        vid.append(vid1)
        filenm=i.pdf
        filename.append(filenm)
        fill=str(i.pdf1).split('/')[-1] #split returns a list
        fil.append(fill)
    mylist1=zip(id,audioname,aud,videoname,vid,filename,fil)
    return render(request,'filedisplay.html',{'data':mylist1})
# zip():returns a list of tuples
# to connect two or more list

def audioedisplay(request):
    v=file1.objects.get()
    if request.method=='POST':
        v.audio=request.POST.get('audioname')
        v.audio1=request.FILES['fileaudio']
        v.video=request.POST.get('videoname')
        v.video1=request.FILES['filevideo']
        v.pdf=request.POST.get('pdfname')
        v.pdf1=request.FILES['filepdf']
        v.save()
        return redirect(filedisplay)
    return render(request,'audioedit.html',{'data':v})




def update_data(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.lname=request.POST.get('lname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        # a.gender=request.POST.get('gender')
        if str(request.POST.get('gender'))=='female'or str(request.POST.get('gender'))=='male':
           a.gender=request.POST.get('gender')
        else:
           a.save()


        a.address=request.POST.get('address')
        # a.dob=request.POST.get('dob')
        if len(str(request.POST.get('dob')))>0:
          a.dob=request.POST.get('dob')
        else:
            a.save()
        a.username=request.POST.get('username')
        a.save()
        return redirect(display)#(display:function)

    return render(request,'edit.html',{'data':a})

def vaccanydelete(request,id):
    a=regmodel.objects.get(id=id)
    a.delete()
    return redirect(funreg)


 # redirect():redirect is a method that is used to redirect from one function to another functions or urls
# def userregisteration(request):
#     if request.method=='POST':
#         a=userreg(request.POST)   #{'username:mariya.'email"abc@gmail,com..}
#         if a.is_valid():
#             us=request.POST.get('username')  #mariya
    #         em=request.POST.get('email')
    #         fname=request.POST.get('first_name')
    #         lname=request.POST.get('last_name')
    #         password=request.POST.get('password')
    #         b=User.objects.create_user(username=us,email=em,first_name=fname,last_name=lname,password=password)
    #         b.save()
    #         return HttpResponse("authenticated user added")
    #     else:
    #         return HttpResponse("user not addedd")
    # else:
    #     form=userreg()
    #     return render(request,'userregister.html',{'form':form})






# is _valid :is used to check the validiy of a form
# cleaned_data:form clean data is where all validated fields are stored it returns a dictionary of
# validated forms input fields and there values

def userregisteration(request):
    if request.method=='POST':
        a=userform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            email=a.cleaned_data['email']
            first=a.cleaned_data['first_name']
            last=a.cleaned_data['last_name']
            password=a.cleaned_data['password']
            conf=a.cleaned_data['conf']
            if password==conf:
                b=User(username=us,email=email,first_name=first,last_name=last)
                b.set_password(password)
                b.save()
                return HttpResponse("register")
            else:
                return HttpResponse("password doesnot match")
        else:
            return HttpResponse('failed')
    else:
        form=userform()
        return render(request,'userregister.html',{'form':form})


def custom_login(request):
    if request.method=='POST':
        form=userlogin(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse('logged in successfully')
            else:
                return HttpResponse('invalid username or password')
        else:
            return HttpResponse ('invalid username or password')

    else:
        form=userlogin()
    return render(request,'loogin.html')

class reg1(generic.CreateView):
    form_class=regform
    template_name = 'register.html'
    success_url = reverse_lazy('login')  #login is a url
    # reverse_lazy
    # it is used to imply a lazy implementation of url
    # used to redirect

class loginn(generic.View):
    form_class=logform
    template_name='login12.html'
    def get(self,request): #to load the login page
        form=self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        if request.method=='POST':
            a=logform(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=models.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return  HttpResponse('login success')
                else:
                        return HttpResponse('login failed')
            return HttpResponse('invalid credentials')


# doubt 9/08/2023
class userregistration(generic.CreateView):
    form_class = userreg
    template_name = 'register1.html'
    success_url = reverse_lazy('login1')






class UserListView(generic.ListView):
    model= Smodels # model name
    template_name='disp.html'
    context_object_name = 'user_list'

# class loginnew1(generic.View):
#     form_class = logform1
#     template_name = 'login13.html'
    #
    # def get(self, request):  # to load loginpage
    #     form = self.form_class
    #     return render(request, self.template_name, {'form': form})
    #
    # def post(self, request):
    #     if request.method == 'POST':
    #         a = logform1(request.POST)
    #         if a.is_valid():
    #             em = a.cleaned_data['email']
    #             ps = a.cleaned_data['password']
    #             b = User.objects.all()
    #             for i in b:
    #                 if em == i.email and ps == i.password:
    #                     return HttpResponse('logged')
    #             else:
    #                 return HttpResponse('FAILED')
    #
    #         return HttpResponse('INVALID')

    # class uselog(generic.View):
    #     form_class1 = logform1
    #     template_name1 = 'login13.html'
    #
    #     def get(self, request):
    #         form = self.form_class1
    #         return render(request, self.template_name1, {'form': form})
    #
    #     def post(self, request):
    #         if request.method == 'POST':
    #             a = logform1(request.POST)
    #             if a.is_valid():
    #                 un = a.cleaned_data['username']
    #                 ps = a.cleaned_data['password']
    #                 b = User.objects.all()
    #                 for i in b:
    #                     if un == i.username and ps == i.password:
    #                         return HttpResponse('Login Success')
    #                 else:
    #                     return HttpResponse('Login Failed')
    #             return HttpResponse('Invalid credentials')

# form_valid()
# to check the form validation we use form valid method
# (commit=false) in form.save commit=false indicates that data is not immediately save to  the database

# 10/08/2023:
# create 3 buttons
# update
# delete
# detail



# delete
class re(generic.DeleteView):
    model = Smodels #model name

    template_name = 'delete.html'
    success_url = reverse_lazy('disp')


class detail(generic.DetailView):
    model=Smodels #(model name)
    template_name = 'detail.html'

class up(generic.UpdateView):
    model=Smodels #your model name
    template_name = 'update.html'
    fields =['name','email']
    success_url = reverse_lazy('disp')


class registerauth(generic.CreateView):
    form_class = userreg
    template_name = 'register1.html'
    success_url = reverse_lazy('authlogin')
    def get(self,request):
        form=self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        if request.method=='POST':
            form=userreg(request.POST)
            if form.is_valid():
                userename=form.cleaned_data['username']
                first_name=form.cleaned_data['first_name']
                last_name=form.cleaned_data['last_name']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                confirm=form.cleaned_data['confirm']

                if password==confirm:
                    user=User(username=userename,first_name=first_name,last_name=last_name,email=email)
                    user.set_password(password)
                    user.save()
                    return  HttpResponse("registered")
                else:
                    return HttpResponse('incorrect password')
            else:
                return HttpResponse("form is not valid")


class authuser(generic.View):
    form_class=authlogin
    template_name='authlogin.html'

    def get(self,request):
        form=self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        if request.method=='POST':
            form=authlogin(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    return HttpResponse("LOGGED")
                else:
                    return HttpResponse("invcalid")
            else:
                return HttpResponse("invalid username")



class UserView(generic.ListView):
    model= User # model name
    template_name='authdisp.html'
    context_object_name = 'create_list'

class fileclass(generic.CreateView):
    form_class = fileform
    template_name = 'file23.html'
    success_url = reverse_lazy('filedisp')


class Filedisp(generic.ListView):
    model=filemodel
    template_name = 'filedispp.html'
    context_object_name = 'files'
    def get(self):
        return filemodel.objects.values('id','image','itemname')


def movie_api():
    with open(r"C:\Users\user\Django project\djangopro\djangoapp\movie.json","r", encoding="utf8") as f :
        data=json.load(f)
    return data
# read re
class movie_passing(APIView):
    def get(self,request):
        data=movie_api()
        return render(request,'rest.html',{'data':data})

def api():
    with open(r"C:\Users\user\Django project\djangopro\djangoapp\files.json","r",encoding="utf8") as e:
        data=json.load(e)
    return data

class api_view(APIView):
    def get(self,request):
        data=api()
        return render(request,'view.html',{'data':data})