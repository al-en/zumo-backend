from django.urls import path
from django.conf.urls import url

from . import views
from zumoapp.models import User

urlpatterns = [
    url(r'^persona$',views.PersonaList.as_view()),
    url(r'^persona/(?P<pk>[0-9]+)$',views.PersonaDetail.as_view()),
    url(r'^persona_proyecto/(?P<proyecto>[0-9]+)/$', views.PersonaListProyecto.as_view()),
    url(r'^red_social$',views.Red_socialList.as_view()),
    url(r'^red_social/(?P<pk>[0-9]+)$',views.Red_socialDetail.as_view()),
    url(r'^proyecto_musical$', views.Proyecto_musicalList.as_view()),
    url(r'^proyecto_musical/(?P<pk>[0-9]+)/$', views.Proyecto_musicalDetail.as_view()),
    url(r'^proyecto_musical/(?P<user>[-\w]+)/$', views.Proyecto_musicalUser.as_view()),
    #url(r'^validaLogin$', User.validaLogin), # no funciona
    url(r'^validaLogin$', views.validaLogin), 
    url(r'^usuario$',views.UserList.as_view()),
    url(r'^usuario/(?P<pk>[-\w]+)$',views.UserDetail.as_view()),
    url(r'^registrar$',views.registrar),
    url(r'^proyecto_detalle/(?P<proyecto>[0-9]+)/$', views.Proyecto_detalleListProy.as_view()),
    url(r'^proyecto_detalleList$', views.Proyecto_detalleList.as_view()),
    url(r'^proyecto_detalleCreate$', views.Proyecto_detalleCreate.as_view()),
    #url(r'^proyecto_detalle/(?P<proyecto>[0-9]+)$', views.getProyectoDetalle),
    url(r'^requisito_nivel$', views.Requisito_nivelList.as_view()),
]