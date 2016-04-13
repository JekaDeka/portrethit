from django.conf.urls import url
from portrethit import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),

]
