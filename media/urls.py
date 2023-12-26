from django.urls import path
from . import views
from report import views as report_views

urlpatterns = [
	path('register/', report_views.RegisterAPI.as_view()),
    path('login/', report_views.LoginAPI.as_view()),
    path('create/', views.CreateMediaSheet.as_view()),
    path('get/<str:name>/<str:sheet>', views.GetDataSheet.as_view()),
    path('post/', views.InsertData.as_view()),
    path('check/', views.Check.as_view()),
    path('location/', views.InsertDataLocation.as_view()),
    path('merge/', views.MergeCells.as_view()),
    path('download/', views.Download.as_view()),
    path('clear-sheet/', views.ClearSheet.as_view()),
    path('create-sheet/', views.CreateNewSheet.as_view()),
    path('media/create', views.CreateMedia.as_view()),
    path('media/update/<int:media_id>/', views.UpdateMedia.as_view()),
    path('media/<int:media_id>/', views.GetMediaByID.as_view()),
    path('media/delete-all', views.DeleteAllMedia.as_view()),
    path('media/', views.GetAllMedia.as_view()),
    path('media-formated/', views.GetAllMediaFormated.as_view()),
    path('report/create', report_views.CreateReport.as_view()),
    path('report/get-all', report_views.GetReports.as_view()),
    path('report/delete-all', report_views.DeleteAllReports.as_view()),
	path('report/download', report_views.DownloadReport.as_view()),
	path('report/download/<int:report_id>', report_views.DownloadReportByID.as_view()),
	path('report/<str:location>/<str:date>', report_views.GetReportByLocationAndDate.as_view()),
	
]
