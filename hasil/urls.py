from django.urls import path
from . import views

urlpatterns = [
     path("",views.index_hasil,name="hasil"),
     path("daftar",views.get_all_hasil,name="daftar"),
     path("report/<int:item_id>/<str:tipe>/",views.get_detail_hasil,name="get_detail_hasil"),
     path("submit-hasil",views.submit_hasil,name="submit_hasil"),
]
