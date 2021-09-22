from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse   # Se importa la libreria para ejecutar llamadas JSON
from rest_framework.decorators import api_view
from rest_framework import generics
from zumoapp.models import Persona, Red_social, Proyecto_musical, Proyecto_musical_detalle, User, \
    Contacto, Nivel, Requisito_nivel, Proyecto_musical_detalle
from zumoapp.serializer import PersonaSerializer, Red_socialSerializer, Proyecto_musicalSerializer, \
    UserSerializer, NivelSerializer, Requisito_nivelSerializer, Proyecto_detalleSerializer, \
    Proyecto_detalleReadSerializer

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import traceback
# Create your views here.

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaListProyecto(generics.ListAPIView):
    #queryset = Proyecto_musical.objects.all()
    serializer_class = PersonaSerializer
    
    def get_queryset(self):
        value = self.kwargs['proyecto']
        return Persona.objects.filter(proyecto_musical_id=value)

class Red_socialList(generics.ListCreateAPIView):
    queryset = Red_social.objects.all()
    serializer_class = Red_socialSerializer

class Red_socialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Red_social.objects.all()
    serializer_class = Red_socialSerializer

class Proyecto_musicalUser(generics.ListCreateAPIView):
    #queryset = Proyecto_musical.objects.all()
    serializer_class = Proyecto_musicalSerializer
    
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        user = self.kwargs['user']
        return Proyecto_musical.objects.filter(user_id=user)

class Proyecto_musicalList(generics.ListCreateAPIView):
    queryset = Proyecto_musical.objects.all()
    serializer_class = Proyecto_musicalSerializer

class Proyecto_musicalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto_musical.objects.all()
    serializer_class = Proyecto_musicalSerializer
    #lookup_fields = ('pk')

class Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto_musical.objects.all()
    serializer_class = Proyecto_musicalSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#@csrf_exempt  # para evitar el error Forbidden (CSRF cookie not set.)
@api_view(['POST'])
def validaLogin(request):
    """user = User()
    user.username = request.data['username']
    user.password = request.data['password']
    print(user)"""
    valido = False
    msj = ""
    proyecto_id = None
    try:
        u = User.objects.get(username=request.data['username'])
        #u = get_object_or_404(User,request.data['username'])
    except:
        u = None
    if u == None:
        msj = "El usuario no existe"
    elif u.password == request.data['password']:
        valido = True
    else:
        msj = "Clave incorrecta"
    if valido:
        p = Proyecto_musical.objects.get(user=request.data['username'])
        proyecto_id = p.id
    return JsonResponse({"valido":str(valido), "mensaje" : msj, "proyecto_id":proyecto_id})

@api_view(['POST'])
def registrar(request):
    try:
        msj = ''
        valido = False
        data = request.data
        username = data['username']
        email = data['email']
        password = data['password']
        proyecto_nombre = data['proyecto_nombre']
        nombre_contacto = data['nombre_contacto']
        apellidop_contacto = data['apellidop_contacto']
        apellidom_contacto = data['apellidom_contacto']
        telefono = data['telefono']

        # Validar si el nombre de usuario existe
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user == None:
            # Validar si el email existe
            try:
                user = User.objects.get(email=email)
            except:
                user = None
            if user == None:
                user = User.objects.create(
                    username = username,
                    email = email,
                    password = password
                )
                
                proyecto = Proyecto_musical.objects.create(
                    nombre = proyecto_nombre,
                    user = user
                )
                
                person = Persona.objects.create(
                    nombres = nombre_contacto,
                    apellido_paterno = apellidop_contacto,
                    apellido_materno = apellidom_contacto,
                    f_activo = True,
                    f_principal = True,
                    proyecto_musical = proyecto
                )

                if telefono != '':
                    Contacto.objects.create(
                        tipo_id = 1,
                        valor = telefono,
                        persona = person
                    )
                if user:
                    valido = True
                    msj = "usuario registrado correctamente"
            else:
                msj = 'El email ingresado ya esta asociado a otra cuenta'
        else:
            msj = 'El nombre de usuario ya existe'
    except Exception:
        msj = 'Ocurrio un error al crear el usuario'
        print(traceback.print_exc())
    return JsonResponse({"valido":str(valido), "mensaje" : msj})

# Niveles
class NivelList(generics.ListCreateAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class NivelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class Requisito_nivelList(generics.ListCreateAPIView):
    #queryset = Requisito_nivel.objects.all()
    serializer_class = Requisito_nivelSerializer
    def get_queryset(self):
        return Requisito_nivel.objects.filter(f_activo=True)

class Requisito_nivelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requisito_nivel.objects.all()
    serializer_class = Requisito_nivelSerializer

class Proyecto_detalleListProy(generics.ListAPIView):
    #queryset = Proyecto_musical_detalle.objects.all()
    serializer_class = Proyecto_detalleReadSerializer
    #lookup_field='proyecto_musical_id'

    def get_queryset(self):
        value = self.kwargs['proyecto']
        return Proyecto_musical_detalle.objects.filter(proyecto_musical_id=value)

# Para GET
class Proyecto_detalleList(generics.ListCreateAPIView):
    queryset = Proyecto_musical_detalle.objects.all()
    serializer_class = Proyecto_detalleReadSerializer

# Para CREATE
class Proyecto_detalleCreate(generics.CreateAPIView):
    queryset = Proyecto_musical_detalle.objects.all()
    serializer_class = Proyecto_detalleSerializer

class Proyecto_detalleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto_musical_detalle.objects.all()
    serializer_class = Proyecto_detalleSerializer
    

# Vista para obtener los datos de los requisitos por nivel
@api_view(['GET'])
def getDetalleRequisitosProyecto(request):
    pass

"""
@api_view(['GET'])
def getProyectoDetalle(request, proyecto):
    lista = Proyecto_musical_detalle.objects.filter(proyecto_musical_id=proyecto)
    return JsonResponse(list(lista), safe=False)
"""
######################################################
# funciones 
######################################################


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)