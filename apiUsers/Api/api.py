from requests import delete
from rest_framework.response import Response
from rest_framework.views import APIView
from apiUsers.models import Ciudad
from .Serializers import Ciudadserializer
from apiUsers.models import Genero
from .Serializers import Generoserializer
from apiUsers.models import Especialidad
from .Serializers import Especialidadserializer
from apiUsers.models import Rol
from .Serializers import Rolserializer
from apiUsers.models import Paciente
from .Serializers import Pacienteserializer
from apiUsers.models import Medico
from .Serializers import Medicoserializer
from apiUsers.models import Familiar
from .Serializers import Familiarserializer
from apiUsers.models import Usuario
from .Serializers import Usuarioserializer
from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view


class CiudadAPIView(APIView):

    def get(self, request):
        cities = Ciudad.objects.all()
        cities_serializer = Ciudadserializer(cities, many=True)
        return Response(cities_serializer.data)


class GeneroAPIView(APIView):

    def get(self, request):
        genders = Genero.objects.all()
        genders_serializer = Generoserializer(genders, many=True)
        return Response(genders_serializer.data)


class EspecialidadAPIView(APIView):

    def get(self, request):
        specialties = Especialidad.objects.all()
        specialties_serializer = Especialidadserializer(specialties, many=True)
        return Response(specialties_serializer.data)


class RolAPIView(APIView):

    def get(self, request):
        roles = Rol.objects.all()
        roles_serializer = Rolserializer(roles, many=True)
        return Response(roles_serializer.data)


class PacienteAPIView(APIView):

    def get(self, request):
        try:

            patients = Paciente.objects.all()
            patients_serializer = Pacienteserializer(patients, many=True)
            data = patients_serializer.data
            if len(data) > 0:
                return Response({
                    "status": "true",
                    "message": "Se ha encontrado con éxito",
                    "response": data})
            else:
                return Response({
                    "status": "true",
                    "messege": "No se encontraron registros",
                    "response": []
                })
        except:
            return Response({
                "status": "false",
                "messege": "Ha ocurrido un error",
                "response": []
            })

        

    def post(self, request):
        try:
            nombres = request.data['nombres']
            apellidos = request.data['apellidos']
            numero_telefono = request.data['numero_telefono']
            print(numero_telefono)
            direccion = request.data['direccion']
            ciudad = Ciudad.objects.get(id=request.data['ciudad'])
            fecha_de_nacimiento = datetime.strptime(
                request.data['fecha_de_nacimiento'], '%Y-%m-%d')
            latitud = request.data['latitud']
            longitud = request.data['longitud']
            patient = Paciente(
                nombres=nombres,
                apellidos=apellidos,
                numero_telefono=numero_telefono,
                direccion=direccion,
                ciudad=ciudad,
                fecha_de_nacimiento=fecha_de_nacimiento.date(),
                latitud=latitud,
                longitud=longitud)
            patient.save()
            return Response({
                "status": "true",
                "message": "se ha guardado con éxito"
            })
        except:
            return Response({
                "status": "false",
                "messege": "Ha ocurrido un error",
                "response": []
            })

@api_view(['GET','PUT','DELETE'])
def editbyid(request, patient_id):
    if request.method=='GET':
        patients = Paciente.objects.filter(id=patient_id)
        patients_serializer = Pacienteserializer(patients, many=True)
        data = patients_serializer.data
        if len(data) > 0:
            return JsonResponse({
                    "status": "true",
                    "message": "Se ha encontrado con éxito",
                    "response": data})
        else:
            return JsonResponse({
                    "status": "true",
                    "messege": "No se encontraron registros",
                    "response": []
                })
    elif request.method=='PUT':
        patient = Paciente.objects.filter(id=patient_id).first()
        patient_serializer = Pacienteserializer(patient,data=request.data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return Response (patient_serializer.data)
        else:
            return Response(patient_serializer.errors)
    elif request.method=='DELETE':
        patient = Paciente.objects.filter(id=patient_id).first()
        patient.delete()
        return Response('user removed')

    




class MedicoAPIView(APIView):

    def get(self, request):
        doctors = Medico.objects.all()
        doctors_serializer = Medicoserializer(doctors, many=True)
        return Response({
            "status": "true",
            "response": doctors_serializer.data
        })

    def post(self, request):
        try:
            nombres = request.data['nombres']
            apellidos = request.data['apellidos']
            numero_telefono = request.data['numero_telefono']
            genero = Genero.objects.get(id=request.data['genero'])
            especialidad = Especialidad.objects.get(
                id=request.data['especialidad'])
            registro = request.data['registro']

            doctor = Medico(
                nombres=nombres,
                apellidos=apellidos,
                numero_telefono=numero_telefono,
                genero=genero,
                especialidad=especialidad,
                registro=registro
            )
            doctor.save()
            return Response({
                "status": "true",
                "message": "se ha guardado con éxito"
            })
        except:
            return Response({
                "status": "false",
                "messege": "Ha ocurrido un error",
                "response": []
            })


class FamiliarAPIView(APIView):

    def get(self, request):
        relatives = Familiar.objects.all()
        relatives_serializer = Familiarserializer(relatives, many=True)
        return Response(relatives_serializer.data)

    def post(self, request):
        try:
            nombres = request.data['nombres']
            apellidos = request.data['apellidos']
            numero_telefono = request.data['numero_telefono']
            email = request.data['email']
            genero = Genero.objects.get(id=request.data['genero'])

            familiar = Familiar(
                nombres=nombres,
                apellidos=apellidos,
                numero_telefono=numero_telefono,
                email=email,
                genero=genero,
            )
            familiar.save()
            return Response({
                "status": "true",
                "message": "se ha guardado con éxito"
            })
        except:
            return Response({
                "status": "false",
                "messege": "Ha ocurrido un error",
                "response": []
            })


class UsuarioAPIView(APIView):

    def get(self, request):
        users = Usuario.objects.all()
        users_serializer = Usuarioserializer(users, many=True)
        return Response(users_serializer.data)
