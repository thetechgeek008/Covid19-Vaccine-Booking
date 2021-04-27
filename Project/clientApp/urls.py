from django.urls import path
from .viewController.authentication import authenticationViews

urlpatterns = [

    path('', authenticationViews.index),
    path('register', authenticationViews.patient_register),
    path('admins', authenticationViews.admin_homepage),
    path('patient', authenticationViews.patient_homepage)

]