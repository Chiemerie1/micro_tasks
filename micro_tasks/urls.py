from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


app_name = "micro_tasks"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.log_in, name="login"),
    path("sign_up/", views.sign_up, name="sign up"),
    path("console/", views.console, name="console")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)