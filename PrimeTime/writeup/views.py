from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import post, postSerializer
from .models import post

# Create your views here.
def writeup_view(request):
    return HttpResponse('<h1>This is a test</h1>')

#Method returns all post items currently in database
@api_view(['GET'])
def postList(request):
    posts = post.objects.all()
    serializer = postSerializer(posts, many=True)
    return Response(serializer.data)

#Method to return a specific post based on it's id
@api_view(['GET'])
def postDetail(request, pk):
    posts = post.objects.get(id=pk)
    serializer = postSerializer(posts, many=False)
    return Response(serializer.data)

#Method to create post items in database
@api_view(['POST'])
def postCreate(request):
    serializer = postSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save

    return Response(serializer.data)

#Method to update post objects in database
@api_view(['POST'])
def postUpdate(request, pk):
    Post = post.objects.get(id=pk)
    serializer = postSerializer(instance=Post, data=request.data)

    if serializer.is_valid():
        serializer.save

    return Response(serializer.data)


#Method to Delete post objects
@api_view(['DELETE'])
def postDelete(request, pk):
    Post = post.objects.get(id=pk)
    Post.delete()


    return Response('Item successfully deleted')