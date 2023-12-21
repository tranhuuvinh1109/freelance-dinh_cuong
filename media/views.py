from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import xlsxwriter
import openpyxl
from openpyxl import load_workbook


class CreateMediaSheet(APIView):
		def get(self, request):
				workbook = xlsxwriter.Workbook('hello.xlsx')
				worksheet = workbook.add_worksheet()
				worksheet.write('A1', 'Hello..')
				worksheet.write('B1', 'Geeks')
				worksheet.write('C1', 'For')
				worksheet.write('D1', 'Geeks')
				workbook.close()
				return Response({'message': 'ok'}, status=status.HTTP_200_OK)

class GetDataSheet(APIView):
    def get(self, request):
        try:
            workbook = load_workbook('hello.xlsx')
            worksheet = workbook.active

            data = []
            for row in worksheet.iter_rows(min_row=2, values_only=True):
                # Assuming the data starts from row 2
                data.append({
                    'column_A': row[0],
                    'column_B': row[1],
                    'column_C': row[2],
                    'column_D': row[3],
                })
						
            return Response({'message': 'ok', 'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class InsertData(APIView):
    def post(self, request):
        try:
            column_A = request.data.get('column_A')
            column_B = request.data.get('column_B')
            column_C = request.data.get('column_C')
            column_D = request.data.get('column_D')

            workbook = load_workbook('hello.xlsx')
            worksheet = workbook.active

            new_row = [column_A, column_B, column_C, column_D]
            worksheet.append(new_row)
            workbook.save('hello.xlsx')

            return Response({'message': 'Data inserted successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class CheckWorker(APIView):
#     def get(self, request):
#         return Response({'message': 'Running...'}, status=status.HTTP_200_OK)