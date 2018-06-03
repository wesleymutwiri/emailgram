from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import permissions
from .models import ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user

class ChatSessionView(APIView):
    '''
    Manage Chat sessions 
    '''
    permission_classes = (permissions.IsAuthenticated,)
    