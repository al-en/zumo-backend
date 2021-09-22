from django.db import models
from django.http import JsonResponse

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Departamento(models.Model):
    #id = models.IntegerField()
    nombre = models.CharField(max_length=45)
    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

class Provincia(models.Model):
    #id = models.IntegerField()
    nombre = models.CharField(max_length=45)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

class Distrito(models.Model):
    #id = models.IntegerField()
    nombre = models.CharField(max_length=45)
    provincia = models.ForeignKey(Provincia, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

class Proyecto_musical(models.Model):
    #id = models.IntegerField()
    nombre = models.CharField(max_length=100,blank=True)
    fecha_formacion = models.DateField(blank=True,null=True)
    descripcion = models.CharField(max_length=1000,blank=True)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL)
    provincia = models.ForeignKey(Provincia, null=True, on_delete=models.SET_NULL)
    distrito = models.ForeignKey(Distrito, null=True, on_delete=models.SET_NULL)
    departamento_str = models.CharField(max_length=45,blank=True)
    provincia_str = models.CharField(max_length=45,blank=True)
    distrito_str = models.CharField(max_length=45,blank=True)
    genero = models.CharField(max_length=100,blank=True)
    redes_sociales = models.CharField(max_length=300,blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    #id = models.IntegerField()
    nombres = models.CharField(max_length=45, blank=True)
    apellido_paterno = models.CharField(max_length=45, blank=True)
    apellido_materno = models.CharField(max_length=45, blank=True)
    sexo = models.CharField(max_length=1, blank=True)
    ocupacion = models.CharField(max_length=100, blank=True)
    ciudad_origen = models.CharField(max_length=45, blank=True)
    edad = models.SmallIntegerField(blank=True)
    fecha_nacimiento = models.DateField(blank=True)
    tipo_identificacion = models.IntegerField(blank=True)
    numero_identificacion = models.CharField(max_length=30, blank=True)
    instrumento = models.CharField(max_length=100, blank=True)
    f_activo = models.BooleanField(default=True, blank=True)
    f_principal = models.BooleanField(default=False, blank=True)
    proyecto_musical = models.ForeignKey(Proyecto_musical, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno

class Contacto(models.Model):
    tipo_id = models.IntegerField()  # 1: celular, 2: email
    valor = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.persona.__str__ + ' - ' + self.valor

class Integrante(models.Model):
    proyecto_musical = models.ForeignKey(Proyecto_musical, null=True, on_delete=models.SET_NULL)
    persona = models.ForeignKey(Persona, null=True, on_delete=models.SET_NULL)
    f_activo = models.BooleanField(default=True)
    f_principal = models.BooleanField(default=False)
    instrumento = models.CharField(max_length=100)  # deberia cambiar a una lista

    class Meta:
        unique_together = ('proyecto_musical','persona')

class Instrumento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=45)

#class Integrante_instrumento

class Nivel(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Requisito_nivel(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=45)
    f_activo = models.BooleanField(default=True)
    nivel = models.ForeignKey(Nivel, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proyecto_genero(models.Model):
    proyecto_musical = models.ForeignKey(Proyecto_musical, null=True, on_delete=models.SET_NULL)
    genero = models.ForeignKey(Genero, null=True, on_delete=models.SET_NULL)

class Red_social(models.Model):
    nombre = models.CharField(max_length=45)
    imagenURL = models.CharField(max_length=100)  # debe ser un selector de imagenes

    def __str__(self):
        return self.nombre

class Proyecto_red_social(models.Model):
    proyecto_musical = models.ForeignKey(Proyecto_musical, null=True, on_delete=models.SET_NULL)
    red_social = models.ForeignKey(Red_social, null=True, on_delete=models.SET_NULL)
    URL = models.CharField(max_length=100)

class Proyecto_musical_detalle(models.Model):
    valor = models.CharField(max_length=200)
    proyecto_musical = models.ForeignKey(Proyecto_musical, null=True, on_delete=models.SET_NULL)
    requisito_nivel = models.ForeignKey(Requisito_nivel, null=True, on_delete=models.SET_NULL)

class Proyecto_musical_detalle_opcion(models.Model):
    codigo = models.IntegerField()
    valor = models.CharField(max_length=100)
    orden = models.IntegerField(null=True)
    f_activo = models.BooleanField()

    """class Meta: 
        unique_together = (('proyecto_musical', 'requisito_nivel'),) 
    """

#Niveles
"""class Nivel1(models.Model):
    maqueta = models.CharField(max_length=100)

class Nivel2(models.Model):
    """
