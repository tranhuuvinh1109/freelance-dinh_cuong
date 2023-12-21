from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import xlsxwriter
import openpyxl
from django.core.exceptions import SuspiciousFileOperation
from openpyxl import load_workbook
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_SAVE_DIR = os.path.join(BASE_DIR, 'data')
class Check(APIView):
    def get(self, request):
        try:

            xlsx_files = [f for f in os.listdir(PATH_SAVE_DIR) if f.endswith('.xlsx') and os.path.isfile(os.path.join(PATH_SAVE_DIR, f))]

            return Response({'message': 'Running...', 'xlsx_files': xlsx_files}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateMediaSheet(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            path = os.path.join(PATH_SAVE_DIR, name + '.xlsx')

            os.makedirs(os.path.dirname(path), exist_ok=True)

            workbook = xlsxwriter.Workbook(path)
            worksheet = workbook.add_worksheet()
            worksheet.write('A1', 'Hello..')
            worksheet.write('B1', 'Geeks')
            worksheet.write('C1', 'For')
            worksheet.write('D1', 'Geeks')

            workbook.close()

            return Response({'message': 'ok', 'name': name + '.xlsx'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetDataSheet(APIView):
    def get(self, request, *args, **kwargs):
        try:
            name = kwargs.get('name')
            path = os.path.join(PATH_SAVE_DIR, name + '.xlsx')

            if not os.path.exists(path):
                raise SuspiciousFileOperation("File not found")

            workbook = load_workbook(path)
            worksheet = workbook.active

            data = []
            for row in worksheet.iter_rows(min_row=2, values_only=True):
                data.append({
                    'column_A': row[0],
                    'column_B': row[1],
                    'column_C': row[2],
                    'column_D': row[3],
                })

            return Response({'message': 'ok', 'data': data}, status=status.HTTP_200_OK)

        except SuspiciousFileOperation as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class InsertData(APIView):
    def post(self, request):
        try:
            column_A = request.data.get('column_A')
            column_B = request.data.get('column_B')
            column_C = request.data.get('column_C')
            column_D = request.data.get('column_D')
            name = request.data.get('name')
            path = os.path.join(PATH_SAVE_DIR, name + '.xlsx')

            workbook = load_workbook(path)
            worksheet = workbook.active

            new_row = [column_A, column_B, column_C, column_D]
            worksheet.append(new_row)
            workbook.save(path)

            return Response({'message': 'Data inserted successfully', "file": path}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class CheckWorker(APIView):
#     def get(self, request):
#         return Response({'message': 'Running...'}, status=status.HTTP_200_OK)