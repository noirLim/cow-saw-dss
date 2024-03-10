from django.urls import path
from . import views

urlpatterns = [
    # kriteria
    path("",views.index_kriteria,name="kriteria"),
    path("daftar",views.get_all_kriteria,name="daftar_kriteria"),
    path("submit",views.submit_kriteria_form,name="submit_kriteria_form"),
    path("edit/<int:item_id>/",views.get_kriteria_by_id,name="get_kriteria_by_id"),
    path("submit/edit/<int:item_id>",views.submit_kriteria_form,name="submit_kriteria_form"),
    path("delete/<int:item_id>/",views.delete_kriteria_by_id,name="delete_kriteria_by_id"),

    # kriteria-sapi
    path("kriteria-sapi",views.index_kriteria_sapi,name="kriteria-sapi"),
    path("kriteria-sapi-daftar",views.get_all_kriteria_sapi,name="daftar_kriteria_sapi"),
    path("kriteria-sapi/submit",views.submit_kriteria_sapi_form,name="submit_kriteria_sapi_form"),
    path("kriteria-sapi-edit/<int:item_id>/",views.get_kriteria_sapi_by_id,name="get_kriteria_sapi_by_id"),
    path("kriteria-sapi/submit/<int:item_id>/",views.submit_kriteria_sapi_form,name="submit_kriteria_sapi_form"),
    path("kriteria-sapi-delete/<int:item_id>/",views.delete_kriteria_sapi_by_id,name="delete_kriteria_sapi_by_id")
]