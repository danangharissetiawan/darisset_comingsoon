from django.contrib import admin
from django.urls import path

from subscribe.views import subscribe

urlpatterns = [
    path('', subscribe, name="home"),
    # path('admin/', admin.site.urls),
]
