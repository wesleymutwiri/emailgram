from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()

def deserialize_user(user):
    """
    Used to deserialize user to JSON format
    """
    return {
        'id': user.id, 'username':user.username, 'email': user.email,
        'first_name': user.first_name, 'last_name':user.last_name
    }

class TrackableDateModel(models.Model):
    '''
    Abstract model to track the creation date for a model
    '''
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    