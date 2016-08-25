from django.conf.urls import url
from wowportret import views

urlpatterns = [
    url(r'^$', views.gallery_page, name='gallery_page'),
    url(r'^test/$', views.test_page, name='test_page'),
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
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    
    url(r'^price/$', views.price_page, name='price_page'),
    url(r'^delivery/$', views.delivery_page, name='delivery_page'),
    url(r'^payment/$', views.payment_page, name='payment_page'),
    url(r'^contacts/$', views.contacts_page, name='contacts_page'),
]
