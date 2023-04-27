from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name="index"),
 #   path('predict',views.predict,name="predict"),
    
    # path('classify_image/', views.classify_image, name='classify_image')

]