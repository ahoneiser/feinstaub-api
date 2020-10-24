from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from sensors.views import AddSensordeviceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/v1/', permanent=False)),
    path('v1/', include("sensors.urls")),
    path('auth/', include("rest_framework.urls", namespace="rest_framework")),
    path('get-auth-token/', obtain_auth_token),
    path('adddevice/', AddSensordeviceView.as_view(), name="adddevice"),
]
