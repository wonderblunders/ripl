"""ripl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from riplInd import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^index', views.v_index, name='index'),	
	url(r'^callme', views.v_callme, name='callme'),
	url(r'^about', views.v_about, name='about'),
	url(r'^make', views.v_make, name='make'),
	url(r'^collection', views.v_collection, name='collection'),
	url(r'^product', views.v_product, name='f_product'),
	url(r'^project', views.v_project, name='project'),
	url(r'^contact', views.v_contact, name='contact'),
	url(r'^support', views.v_support, name='support'),
	url(r'^faq', views.v_faq, name='faq'),
	url(r'^itemfetch', views.v_itemfetch, name='itemfetch'),
	url(r'^support', views.v_support, name='support'),
	url(r'^fabric', views.v_fabric, name='fabric'),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
