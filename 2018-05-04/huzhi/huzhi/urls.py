from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^qa/', include('qa.urls')),
    url(r'^admin/', admin.site.urls),
]