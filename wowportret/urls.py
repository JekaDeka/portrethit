from django.conf.urls import url
from wowportret import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^art/$', views.art_page, name='art_page'),
    url(r'^classic/$', views.classic_page, name='classic_page'),
    url(r'^holst/$', views.holst_page, name='holst_page'),
    url(r'^glavnaya/$', views.index_page, name='index_page'),
    url(r'^maslo/$', views.maslo_page, name='maslo_page'),
    url(r'^maslo2/$', views.maslo2_page, name='maslo2_page'),
    url(r'^popart/$', views.popart_page, name='popart_page'),
    url(r'^portret/$', views.portret_page, name='portret_page'),

]
