from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.AllComments.as_view()),
    path('add_comment/', views.AllComments.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),  # 'as.view()' b/c we are using class views.
    path('reply/', views.AllReplies.as_view()),
    path('add_reply/', views.AllReplies.as_view()),
    path('reply/<int:pk>/', views.ReplyDetail.as_view()),


]
