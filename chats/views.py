from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import permissions
from .models import ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user

# views 

class ChatSessionView(APIView):
    '''
    Manage Chat sessions 
    '''
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        '''
        Create a new chat session
        '''
        user = request.user 
        chat_session = ChatSession.objects.create(owner=user)

        return Response({
            'status': 'SUCCESS','uri':chat_session.uri,
            'message': 'New chat session created'
        })
    def 