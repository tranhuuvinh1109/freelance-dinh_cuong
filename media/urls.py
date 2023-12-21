from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateMediaSheet.as_view(), name='create'),
    path('get/', views.GetDataSheet.as_view(), name='get'),
    path('post/', views.InsertData.as_view(), name='post'),
    path('check/', views.Check.as_view(), name='post'),
]
