from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.AllComments.as_view()),
    path('comments/comment/<int:pk>/', views.CommentDetail.as_view()),  # 'as.view()' b/c we are using class views.
]
