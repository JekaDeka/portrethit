from django.conf.urls import url
from wowportret import views

urlpatterns = [
    url(r'^$', views.gallery_page, name='gallery_page'),
    url(r'^art/$', views.art_page, name='art_page'),
    url(r'^classic/$', views.classic_page, name='classic_page'),
    url(r'^holst/$', views.holst_page, name='holst_page'),
    url(r'^maslo/$', views.maslo_page, name='maslo_page'),
    url(r'^maslo2/$', views.maslo2_page, name='maslo2_page'),
    url(r'^popart/$', views.popart_page, name='popart_page'),
    url(r'^portret/$', views.portret_page, name='portret_page'),
    url(r'^baget/$', views.baget_page, name='baget_page'),
    url(r'^thankyou/$', views.thank_page, name='thank_page'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_page, name='item_page'),
    url(r'^gallery/$', views.gallery_page, name='gallery_page'),
    url(r'^gallery/(?P<pk>[0-9]+)/$',
        views.gallery_detail, name='gallery_detail'),
]
