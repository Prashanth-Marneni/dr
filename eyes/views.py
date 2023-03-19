from django.shortcuts import render, HttpResponse, redirect
from eyes.models import Information
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.core.files.storage import FileSystemStorage


from keras.models import load_model
import cv2
import numpy as np
from keras.preprocessing import image
import tensorflow_hub as hub
import tensorflow as tf
from PIL import Image
from tensorflow import Graph
import matplotlib.image as mpimg

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'signin.html')

def details(request):
    return render(request,"details.html")
def test(img, model):
    img1 = mpimg.imread(img)
    img1 = cv2.resize(img1, (224, 224), 3)
    img1 = np.array(img1)/255.0
    img1[np.newaxis, ...].shape
    prediction = model.predict(img1[np.newaxis, ...])
    prediction = np.argmax(prediction)
    if (prediction == 0):
        res = 'no dr'
    elif (prediction == 1):
        res = 'mild dr'
    elif (prediction == 2):
        res = 'moderate dr'
    elif (prediction == 3):
        res = 'severe'
    else:
        res = 'proliferate'
    return res


def predict(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        leftimg = request.FILES.get('file1')
        rightimg = request.FILES.get('file2')
        model = tf.keras.models.load_model('final.h5', custom_objects={
                                           'KerasLayer': hub.KerasLayer})
        res1 = test(leftimg, model)
        res2 = test(rightimg, model)
        fs=FileSystemStorage()
        f1 = fs.save(leftimg.name,leftimg)
        f2 = fs.save(rightimg.name,rightimg)
        f1=fs.url(leftimg)
        print(f1)
        f2 = fs.url(rightimg)
        print(f2)
        obj = Information(name=name, email=email, phone=phone,
                          leftimg=leftimg, rightimg=rightimg,leftdr = res1,rightdr = res2)
        obj.save()
        context = {"name":name,"email":email,"phone":phone,"leftimg":f1,"rightimg":f2,"leftdr":res1,"rightdr":res2}
        return render(request, 'result.html', context)

    return render(request, 'details.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, "hey your account has been created successfully")
        return redirect('signin')
    return render(request, 'signup.html')


def doctor(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        info = Information.objects.filter(phone=phone)
        context = {'info':info}
        return render(request,'doctor.html',context)
    info = Information.objects.all()
    context = {'info': info}
    return render(request, 'doctor.html', context)


def signin(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            auth_login(request, user)
            info = Information.objects.all()
            context = {'info': info}
            return render(request, 'doctor.html',context)
        else:
            messages.error(request, 'Bad Crendentials')
            return redirect('index')
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('home')


def Edit(request):
    info = Information.objects.all()
    context = {'info': info}
    return redirect(request, 'doctor.html', context)


def Update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        leftimg = request.FILES.get('file1')
        rightimg = request.FILES.get('file2')
        obj = Information(id=id, name=name, email=email,
                          phone=phone, leftimg=leftimg, rightimg=rightimg)
        obj.save()
        return redirect('doctor')
    return redirect("doctor")


def Delete(request, id):
    info = Information.objects.filter(id=id).delete()
    return redirect('doctor')


def Result(request):
    info = Information.objects.filter(id=3)
    context = {"info": info}
    print(info)
    return render(request, "result.html", context)
