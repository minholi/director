"""director URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from controlcenter.views import controlcenter
from director import settings

admin.site.site_header = 'Director'
admin.site.site_title = 'Director'
admin.site.site_url = None

urlpatterns = [
    path('', admin.site.urls),
    path('dashboard/', controlcenter.urls),
    path('suporte/', include('suporte.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

# Static files during development
# https://docs.djangoproject.com/en/2.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
