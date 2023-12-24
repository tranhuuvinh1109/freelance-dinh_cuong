from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateMediaSheet.as_view(), name='create'),
    path('get/<str:name>/<str:sheet>', views.GetDataSheet.as_view(), name='get'),
    path('post/', views.InsertData.as_view(), name='post'),
    path('check/', views.Check.as_view(), name='post'),
    path('location/', views.InsertDataLocation.as_view(), name='post'),
    path('merge/', views.MergeCells.as_view(), name='post'),
    path('download/', views.Download.as_view(), name='post'),
    path('clear-sheet/', views.ClearSheet.as_view(), name='post'),
    path('create-sheet/', views.CreateNewSheet.as_view(), name='sheet'),
    path('media/create', views.CreateMedia.as_view(), name='sheet'),
    path('media/update/<int:media_id>/', views.UpdateMedia.as_view(), name='sheet'),
    path('media/<int:media_id>/', views.GetMediaByID.as_view(), name='sheet'),
    path('media/delete-all', views.DeleteAllMedia.as_view(), name='sheet'),
    path('media/', views.GetAllMedia.as_view(), name='sheet'),
    path('media-formated/', views.GetAllMediaFormated.as_view(), name='sheet'),
]
