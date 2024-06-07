"""AgoraProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from AgoraApp.views import TranscribeAudio,DebateUserListCreate,DebateUserDetail,get_user_by_username,delete_user_by_username

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transcribe/', TranscribeAudio.as_view(), name='transcribe-audio'),
    path('debateusers/', DebateUserListCreate.as_view(), name='debateuser-list-create'),
    path('debateusers/<int:pk>/', DebateUserDetail.as_view(), name='debateuser-detail'),
    path('debateusers/username/<str:username>/', get_user_by_username, name='get-user-by-username'),
    path('debateusers/username/<str:username>/delete/', delete_user_by_username, name='delete-user-by-username'),
]