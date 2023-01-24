from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.permissions import IsAuthenticated
from models.models import Chat
from django.contrib.auth.models import User

from django.db import connection

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list(req):
    data=[]
    user=req.user
    with connection.cursor() as cursor:
        cursor.execute("select concat(au.first_name , au.last_name) as name ,d.u_id from (SELECT DISTINCT from_id as u_id FROM models_chat where to_id = {} UNION SELECT DISTINCT to_id as user_id FROM models_chat where from_id={}) d join auth_user au on d.u_id=au.id;".format(user.id,user.id))
        rows = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]
        data = [dict(zip(column_names, row)) for row in rows]
    return Response(data)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def add(req):
    user=req.user
    from_id=user.id
    to_id=int(req.POST['to_id'])
    ident="{}_{}".format(from_id,to_id)
    if to_id<from_id :
        ident="{}_{}".format(to_id,from_id)
    toUser=User.objects.get(id=to_id)
    chat=Chat()
    chat.ident=ident
    chat.from_id=from_id
    chat.to_id=to_id
    chat.senderName=user.first_name
    chat.receiverName=toUser.first_name
    chat.message=req.POST['msg']
    chat.save()
    chats=Chat.objects.filter(ident=ident).values()
    return Response(chats)
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def single(req):
    user=req.user
    from_id=user.id
    to_id=int(req.POST['to_id'])
    ident="{}_{}".format(from_id,to_id)
    if to_id<from_id :
        ident="{}_{}".format(to_id,from_id)
    chats=Chat.objects.filter(ident=ident).values()
    return Response(chats)
    
    
    
