from django.conf.urls import url
from .views import *

urlpatterns =[

    url(r'^$', index, name='index'),
    
    url(r'^display_laptop$', display_laptops, name='display_laptops'),

    url(r'^display_desktop$', display_desktops, name='display_desktops'),

    url(r'^display_mobile$', display_mobiles, name='display_mobiles'),

    url(r'^add_laptop$', add_laptop, name='add_laptop'),

    url(r'^add_desktop$', add_desktop, name='add_desktop'),

    url(r'^mobile$', add_mobile, name='add_mobile'),
]