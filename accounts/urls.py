from django.urls import path

from . import views

urlpatterns = [
    path('signup.html/', views.SignUpView.as_view(), name = 'signup.html' ),
]
