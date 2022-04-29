"""recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views as views
 
urlpatterns = [
    path('',views.home, name='home'),
    path('Dashbord/',views.coming, name='Dashbord'),
    path('Privacy_Policy/',views.coming, name='Privacy_Policy'),
    path('Recipes/',views.coming, name='Recipes'),
    path('terms_and_condition/',views.coming, name='terms_and_condition'),
    path('Bookmark/',views.coming, name='Bookmark'),
    path('Courses/',views.coming, name='Courses'),
    path('Account/',views.coming, name='Account'),
    path('user_settings/',views.coming, name='user_settings'),
    path('<slug:type>/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
