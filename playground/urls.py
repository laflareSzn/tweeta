from django.urls import path, include
from tweet import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'e', views.TweetViewSet, basename='tweets')
router.register(r'comments', views.CommentViewSet, basename='comments')
router = SimpleRouter()
urlpatterns = [

    path('', include(router.urls)),

    # path('list/', views.TweetList.as_view()),
    # path('<int:pk>/', views.TweetDetail.as_view()),
    # path("comment/", views.CommentList.as_view()),
    # path("comment/<int:pk>/", views.CommentDetail.as_view())
]