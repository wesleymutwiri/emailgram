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
    
    def patch(self, request, *args, **kwargs):
        '''
        Add a user to a chat session
        '''
        User = get_user_model()
        uri = kwargs['uri']
        username = request.data['username']
        user = User.objects.get(username=username)
        chat_session = ChatSession.objects.get(uri=uri)
        owner = chat_session.owner 
        
        # function to allow only none owners to join the chat room
        
        if owner != user: 
            chat_session.membeers.get_or_create(user=user, chat_session=chat_session)
        
        owner = deserialize_user(owner)
        members = [
            deserialize_user(chat_session.user)
            for chat_session in chat_session.membeers.all()
        ]
        # function that makes the owner th first member of the group
        members.insert(0,owner)

        return Response({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined this chat' %user.username,
            'user': deserialize_user(user)
        })

class ChatSessionMessageView(APIView):
    '''
    Create/get chat session messages 
    '''

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        '''
        return all messages in a chat session
        '''
        uri = kwargs['uri']
        chat_session = ChatSession.objects.get(uri=uri)
        message = [chat_session_message.to_json() 
            for chat_session_message in chat_session.messages.all()]
        return Response({
            'id': chat_session.id, 'uri':chat_session.uri, 
            'messages': messages
        })

    def post(self, request,*args, **kwargs):
        '''
        create a new message in a chat session
        '''
        uri = kwargs['uri']
        message = request.data['message']
        user = request.user 
        chat_session = ChatSession.objects.get(uri=uri)

        ChatSessionMessage.objects.create(
            user=user, chat_session=chat_session, message=message
        )

        return Response({
            'status': 'SUCCESS', 'uri':chat_session.uri, 'message':message, 'user':deserialize_user(user)
        })