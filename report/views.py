from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import os
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseNotFound
from report.create_word import clear_word_document, create_report_docx
from report.sendMail import send_mail_to_admin
from report.transform_object import transform_report
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.db.models import Q


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_SAVE_DIR = os.path.join(BASE_DIR, 'manage/media')

class UserSerializerNested(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    avatar = serializers.CharField()
    username = serializers.CharField()

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializers = UserSerializer(data=data)

        if serializers.is_valid():
            serializers.save()
            return Response({
                'status': 200,
                'message': 'User registered successfully, please check your Email to confirm',
                'data': serializers.data
            })

        return Response({
            'status': 400,
            'message': 'User registration failed, please try again',
            'data': serializers.errors
        })

 
class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = User.objects.filter(email=email)

            if user.exists() and user.count() == 1:
                user_data = user.first()

                if user_data.check_password(password):
                    return Response({
                        'status': 200,
                        'message': 'User login successful',
                        'data': {
                            'user': UserSerializer(user_data).data
                        }
                    })
            else:
                return Response({
                    'status': 400,
                    'message': 'Wrong password or email, please try again',
                })
        else:
            return Response({
                'status': 400,
                'message': 'Invalid input, please provide valid email and password',
            })
        
class CreateReport(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = ReportSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            report_data = serializer.validated_data

            serializer.save()
            send_mail_to_admin(serializer.data['location'], ['dinhcuongbkdn96@gmail.com', 'tranhuudu113@gmail.com'], serializer.data['date_report'])
            return Response(
                {'message': 'Report created successfully', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class GetReports(APIView):
    def get(self, request, *args, **kwargs):
        try:
            reports = Report.objects.all()
            serializer = ReportSerializer(reports, many=True)
            # report = {
            #     "location": "QNN/NTG",
            #     "start_day": "25/12/2023",
            #     "end_day": "26/12/2023",
            #     "device": "BT",
            #     "cable": "BT",
            #     "power": "SC",
            #     "report": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            #     "other_job": "Other job details go here.",
            #     "exist": "Existing conditions description.",
            #     "propose": "Proposed actions or solutions.",
            #     "creator": "Tran huu Vinh",
            #     "save": "NTG-26"
            # }
            # path = os.path.join(PATH_SAVE_DIR)
            # os.makedirs(os.path.dirname(path), exist_ok=True)
            # create_report_docx("vinh.docx",path, report)
            # send_mail_to_admin(report['location'], ['dinhcuongbkdn96@gmail.com', 'tranhuudu113@gmail.com'], report['start_day'])

            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetReportByLocationAndDate(APIView):
    def get(self, request, *args, **kwargs):
        try:
            location = kwargs.get('location')
            location = f"QNN/{location}"
            date_report = kwargs.get('date').replace("-", "/")
            reports = Report.objects.filter(location=location, date_report=date_report)
            serializer = ReportSerializer(reports, many=True)

            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DeleteAllReports(APIView):
    def delete(self, request, *args, **kwargs):
        try:
            Report.objects.all().delete()

            return Response(
                {'message': 'All reports deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_reports_by_location_and_date(location, date_report):
    try:
        reports = Report.objects.filter(location=location, date_report=date_report)
        serializer = ReportSerializer(reports, many=True)

        return serializer.data

    except Exception as e:
        return {'message': str(e)}   
class DownloadReport(APIView):
    def get(self, request):
        res = get_reports_by_location_and_date("QNN/TKT", "26/12/2023")
        
        if len(res) > 0:
            path = os.path.join(PATH_SAVE_DIR)
            transform_reported = transform_report(res[0])
            create_report_docx("vinh.docx", path, transform_reported)
            file_path = os.path.join(BASE_DIR, 'manage/media', "vinh.docx")

            try:
                with open(file_path, 'rb') as f:
                    file_data = f.read()

                response = HttpResponse(file_data, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'attachment; filename=vinh.docx'

            except IOError:
                response = HttpResponseNotFound('<h1>File not exist</h1>')

            return response

        return Response({'message': 'No reports found for the given location and date.'}, status=status.HTTP_404_NOT_FOUND)

class DownloadReportByID(APIView):
    def get(self, request, report_id, *args, **kwargs):
        res = Report.objects.get(pk=report_id)

        if res:
            path = os.path.join(PATH_SAVE_DIR)
            file_path = os.path.join(BASE_DIR, 'manage/media', "report.docx")
            serializer = ReportSerializer(res)
            clear_word_document(file_path)
            transformed_report = transform_report(serializer.data)
            create_report_docx("report.docx", path, transformed_report)

            try:
                with open(file_path, 'rb') as f:
                    file_data = f.read()

                response = HttpResponse(file_data, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'attachment; filename=report.docx'

            except IOError:
                response = HttpResponseNotFound('<h1>File not exist</h1>')

            return response

        return Response({'message': 'No report found for the given ID.'}, status=status.HTTP_404_NOT_FOUND)