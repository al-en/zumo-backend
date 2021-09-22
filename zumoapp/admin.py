from django.contrib import admin
import zumoapp.models as mod

# Register your models here.
admin.site.register(mod.Persona)
admin.site.register(mod.Departamento)
admin.site.register(mod.Provincia)
admin.site.register(mod.Distrito)
admin.site.register(mod.Proyecto_musical)
admin.site.register(mod.Contacto)
#admin.site.register(mod.Integrante)
admin.site.register(mod.Instrumento)
admin.site.register(mod.Nivel)
admin.site.register(mod.Requisito_nivel)
admin.site.register(mod.Genero)
admin.site.register(mod.Proyecto_genero)
admin.site.register(mod.Red_social)
admin.site.register(mod.Proyecto_red_social)
admin.site.register(mod.Proyecto_musical_detalle)