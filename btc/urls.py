"""btc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.flatpages import views
from static_pages.views import (index, contact, login_view, logout_view, validate_username, validate_email, validate_password, register )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', include('dashboard.urls', namespace="profile")),

    # # dynamic pages
    url(r'^contact-us/$', contact, name='contact'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^ajax/username-validate/$', validate_username, name='username'),
    url(r'^ajax/email-validate/$', validate_email, name='email'),
    url(r'^ajax/password-validate/$', validate_password, name='password'),

    # flat pages
    url(r'^about-us/$', views.flatpage, {'url': '/about-us/'}, name='about'),
    url(r'^$', views.flatpage, {'url': '/index/'}, name='index'),
    url(r'^(?P<ref>\w+)$', index),
    url(r'^how-it-works/$', views.flatpage, {'url': 'how-it-works/'}, name='hiw'),
    url(r'^terms/$', views.flatpage, {'url': '/terms/'}, name='terms'),
    url(r'^faq/$', views.flatpage, {'url': '/faq/'}, name='faq'),

    # referal links
    url(r'^(?P<ref>\w+)/register/$', register, name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT
                          )
