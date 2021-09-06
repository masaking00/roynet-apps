from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    #path('upload/', views.upload.as_view(), name='upload'),
    path('all',views.FoundItemsView,name="all"),
    path('list/',views.FindItemView.as_view(),name="list"),
    path('list/<int:pk>/update/',views.FoundItemUpdateView.as_view(),name="update"),
]
