from django.conf.urls import url
from gestaoProjetos import views

app_name = 'gestaoProjetos'
urlpatterns = [
    url(r'^$', views.showcase, name='index'),
    url(r'^showcase$', views.showcase, name='showcase'),
    url(r'^projetos/(?P<projeto_id>\d+)/$', views.detalhes_projeto, name='detalhes_projeto'),
]
