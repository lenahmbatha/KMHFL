from django.urls import path 
from django.conf.urls import url
from . import views

urlpatterns = [
	path('' , views.index , name = "index"),
	path('register.html/' , views.register , name = "register"),
	path('forgot-password.html/' , views.forget , name = "forget"),
 	path('index.html' , views.home , name = "home"),
  	path('tables.html' , views.table , name = "table"),
	# path('registerUser/' , views.addUser , name = "registerUser"),
	# path('verifyUser/' , views.verifyUser , name = "authenticate"),
]