from rest_framework import serializers
from zumoapp.models import Persona, Proyecto_musical, Red_social, Integrante, \
Proyecto_musical_detalle, User, Nivel, Requisito_nivel, Proyecto_musical_detalle


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
        #fields = ('id','nombres','apellido_paterno','apellido_materno','sexo','ocupacion','ciudad_origen','edad','fecha_nacimiento','tipo_identificacion','numero_identificacion')

class Red_socialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Red_social
        fields = '__all__'

class IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrante
        fields = '__all__'

class Proyecto_musicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto_musical
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'

class Requisito_nivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisito_nivel
        fields = '__all__'

class Proyecto_detalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto_musical_detalle
        fields = '__all__'

class Proyecto_detalleReadSerializer(serializers.ModelSerializer):
    #requisito_nivel = serializers.StringRelatedField(many=False)
    requisito_nivel = Requisito_nivelSerializer(read_only=False)

    class Meta:
        model = Proyecto_musical_detalle
        fields = '__all__'