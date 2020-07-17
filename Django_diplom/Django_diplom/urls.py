"""Django_diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from django.conf import settings
from django.urls import include

from Shop.views import main, gadgets, product, accessories, cart
from app_users.views import user_register, user_logout, user_login


urlpatterns = [
    path('', main),
    path('index/', main, name='main'),
    path('admin/', admin.site.urls),
    path('accessories/', accessories, name='accessories'),
    path('cart/', cart, name='cart'),

    url(r'^account/register/$', user_register, name='user_register'),
    url(r'^account/login/$', user_login, name='user_login'),
    url(r'^account/logout/$', user_logout, name='user_logout'),
    url(r'section/(?P<slug>[\w-]+)/$', gadgets, name='index'),
    url(r'(?P<slug>[\w-]+)/$', product, name='product')
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)