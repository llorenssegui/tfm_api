"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from django_rest.quickstart import views

router = routers.DefaultRouter()
#router.register(r'professors', views.ProfessorViewSet)
#router.register(r'assignatures', views.AssignaturaViewSet)
#router.register(r'cursos', views.CursViewSet)
#router.register(r'alumnes', views.AlumneViewSet)
#router.register(r'centres', views.CentreViewSet)
#router.register(r'activitats', views.ActivitatViewSet)
#router.register(r'qualificacions', views.QualificacioViewSet)
#router.register(r'trimestres', views.TrimestreViewSet)
router.register(r'anysacademics', views.AnyAcademicViewSet)
#router.register(r'grups', views.GrupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^professors/$', views.ProfessorViewList.as_view()),
    url(r'^professors/(?P<pk>[0-9]+)/$', views.ProfessorViewDetail.as_view()),
    url(r'^assignatures/$', views.AssignaturaViewList.as_view()),
    url(r'^assignatures/(?P<pk>[0-9]+)/$', views.AssignaturaViewDetail.as_view()),
    url(r'^cursos/$', views.CursViewList.as_view()),
    url(r'^cursos/(?P<pk>[0-9]+)/$', views.CursViewDetail.as_view()),
    url(r'^centres/$', views.CentreViewList.as_view()),
    url(r'^centres/(?P<pk>[0-9]+)/$', views.CentreViewDetail.as_view()),
    url(r'^alumnes/$', views.AlumneViewList.as_view()),
    url(r'^alumnes/(?P<pk>[0-9]+)/$', views.AlumneViewDetail.as_view()),
    url(r'^activitats/$', views.ActivitatViewList.as_view()),
    url(r'^activitats/(?P<pk>[0-9]+)/$', views.ActivitatViewDetail.as_view()),
    url(r'^trimestres/$', views.TrimestreViewList.as_view()),
    url(r'^trimestres/(?P<pk>[0-9]+)/$', views.TrimestreViewDetail.as_view()),
    url(r'^anysacademics/$', views.AnyAcademicViewList.as_view()),
    url(r'^anysacademics/(?P<pk>[0-9]+)/$', views.AnyAcademicViewDetail.as_view()),
    url(r'^grups/$', views.GrupViewList.as_view()),
    url(r'^grups/(?P<pk>[0-9]+)/$', views.GrupViewDetail.as_view()),
    url(r'^qualificacions/$', views.QualificacionsViewList.as_view()),
    url(r'^qualificacions/(?P<pk>[0-9]+)/$', views.QualificacionsViewDetail.as_view()),
    url(r'^cambiarcontrassenya/(?P<pk>[0-9]+)/$', views.CambiarContrassenyaView.as_view()),
]