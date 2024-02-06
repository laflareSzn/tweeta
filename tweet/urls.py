# from django.urls import path
# from . import views
# urlpatterns = [
#     path('list/', views.tweet_list),
#     path('<int:pk>/', views.tweet_details),
#     path('', views.tweets),
# ]
from django.urls import path, include
from rest_framework_nested import routers

from tweet import views
from rest_framework.router import SimpleRouter, DefaultRouter


router = routers.DefaultRouter()
comment_router=routers.NestedDefaultRouter(router, "comments", lookup:"tweet-comments")
comment_router.register ("comments", views.CommentViewSet, basename='tweet-comment')
router = SimpleRouter()
router.register("tweets", views.TweetViewSet)


urlpatterns = [

    path('', include(router.urls)),

    # path('list/', views.TweetList.as_view()),
    # path('<int:pk>/', views.TweetDetail.as_view()),
    path("comment/", views.CommentList.as_view()),
    path("comment/<int:pk>/", views.CommentDetail.as_view()),

]