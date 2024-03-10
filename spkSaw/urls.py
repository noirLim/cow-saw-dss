from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index_home,name="home"),
    path('admin/', admin.site.urls),
    path("sapi/",include("sapi.urls")),
    path("kriteria/",include("kriteria.urls")),
    path("nilai/",include("nilai.urls")),
    path("hasil/",include("hasil.urls")),
]
