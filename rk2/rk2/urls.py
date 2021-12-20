"""rk2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('computers/<int:id>',  views.computer, name='computer'),
    path('computer_add/', views.computer_add, name='computer_add'),
    path('computer_edit/<int:id>', views.computer_edit, name='computer_edit'),
    path('computer_delete/<int:id>', views.computer_delete, name='computer_delete'),
    path('computers/os_add/<int:id>', views.os_add, name='os_add'),
    path('os_edit/<int:id>', views.os_edit, name='os_edit'),
    path('os_delete/<int:id>', views.os_delete, name='os_delete'),
    path('report/', views.report, name="report"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()