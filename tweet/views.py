# from django.http import HttpResponse
# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Tweet, Comment
from .serializers import TweetSerializer, CommentSerializer


# from django.shortcuts import get_object_or_404

# from tweet.models import Tweet


# Create your views here.

# class TweetList(APIView):
#     def get(self):
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = TweetSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()


# # to support request
# # @api_view(['GET', 'POST'])
# # def tweets(request):
# #     if request.method == 'GET':
# #         tweets = Tweet.objects.all()
# #         serializer = TweetSerializer(tweets, many=True)
# #         return Response(serializer.data, status=status.HTTP_200_OK)
# #     elif request.method == 'POST':
# #         serializer = TweetSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def tweet_detail(request, pk):
#     tweet = get_object_or_404(Tweet, pk=pk)
#     if request.method == 'GET':
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = TweetSerializer(tweet, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# def tweet_list(request, pk):
#     return None

class TweetList(ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentList(ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
