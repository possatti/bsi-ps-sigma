from django.conf.urls import url
from gestaoProjetos import views

app_name = 'gestaoProjetos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
