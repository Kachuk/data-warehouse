from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views
from django_auth import views as my_auth_views

router = routers.DefaultRouter()
#router.register(r'snippets', snippet_api_views.SnippetViewSet)



 
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', my_auth_views.home, name='home'),
    path('register/', my_auth_views.register, name='register'),
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]