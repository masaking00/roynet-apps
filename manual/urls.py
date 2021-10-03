from django.urls import path
from . import views

app_name = 'manual'

urlpatterns = [
    path('list/',views.PostListView.as_view(),name="post"),
    path('<int:pk>/',views.PostDetailView.as_view(),name="post_detail"),
]
