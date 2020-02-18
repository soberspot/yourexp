from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from lending import views

urlpatterns = [

    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    # re_path(r'^admin', admin.site.urls),
    # path('about/', TemplateView.as_view(template_name="about.html")),
    # path('contact/', TemplateView.as_view(template_name="contact.html")),
]
