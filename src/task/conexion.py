from src.app.celery import app
from src.app import celery as cele
import time
import random
import pywhatkit
from datetime import datetime
# @app.task
# def conectar(n):
#     time.sleep(n)
#     print('Conectando! Papi')
#     return

class conexion:

    @app.task
    def conectar(data, tiempo):
        print('tarea conectar!')
        return
    
    def desconectar():
        print('Desconectado!')
        return