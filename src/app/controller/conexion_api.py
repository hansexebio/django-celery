from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework import status
from src.task.conexion import conexion
import time
from datetime import datetime
import pywhatkit

class Conexion(viewsets.ViewSet):
    def estado_conexion(self, request) -> JsonResponse:
        # request data -> segundo : int , data : str
        print('conexion!')
        conexion.conectar.apply_async(countdown=request.data['segundo'], args=[request.data['data'], request.data['segundo']])
        return JsonResponse(
                {'success': True, 'message': 'Bien'},
                status=status.HTTP_200_OK)