from rest_framework import serializers
from apiUsers.models import Usuario
from apiUsers.models import Ciudad
from apiUsers.models import Genero
from apiUsers.models import Especialidad
from apiUsers.models import Rol
from apiUsers.models import Paciente
from apiUsers.models import Medico
from apiUsers.models import Familiar
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

class Ciudadserializer(serializers.ModelSerializer):
    class Meta:
        model= Ciudad
        fields = '__all__'

class Generoserializer(serializers.ModelSerializer):
    class Meta:
        model= Genero
        fields = '__all__'

class Especialidadserializer(serializers.ModelSerializer):
    class Meta:
        model= Especialidad
        fields = '__all__'

class Rolserializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields = '__all__'

class Pacienteserializer(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields = '__all__'

class Medicoserializer(serializers.ModelSerializer):
    class Meta:
        model= Medico
        fields = '__all__'
        
class Familiarserializer(serializers.ModelSerializer):
    class Meta:
        model= Familiar
        fields = '__all__'

class Usuarioserializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields = '__all__'

