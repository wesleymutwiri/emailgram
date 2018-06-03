from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
# from django.views.generic import TemplateView


urlpatterns = [
    # url(r'^$', views.index, name= 'index'),
    path('chats/', views.ChatSessionView.as_view()),
    path('chats/<url>/', views.ChatSessionView.as_view()),
    path('chats/<url>/messsages/', views.ChatSessionMessageView.as_view()),
]

