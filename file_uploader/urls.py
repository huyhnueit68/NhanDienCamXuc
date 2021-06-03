from django.conf.urls import url

from . import views
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('css/index.css', TemplateView.as_view(
        template_name='index.css',
        content_type='text/css')
    ),
    url(r'^$', views.fileUploaderView),
]