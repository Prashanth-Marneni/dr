from django.contrib import admin
from django.urls import path,include
from eyes import views
urlpatterns = [
    path('',views.index,name='home'),
     path('login',views.login,name='login'),
     path('home',views.index,name='home'),
     path('details',views.details,name='details'),
     path('signup',views.signup,name='signup'),
     path('signin',views.signin,name='signin'),
     path('signout',views.signout,name='signout'),
     path('predict',views.predict,name='predict'),
     path('doctor',views.doctor,name="doctor"),
     path('edit',views.Edit,name="edit"),
     path('update/<str:id>',views.Update,name="update"),
     path('delete/<str:id>',views.Delete,name="delete"),
     path("result",views.Result,name="result"),
     path("index",views.index,name="index")
]