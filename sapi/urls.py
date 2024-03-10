from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_sapi,name="sapi"),
    path("daftar",views.get_all_sapi,name="get_all_sapi"),
    path("submit",views.submit_sapi_form,name="submit_sapi_form"),
    path("edit/<int:item_id>/",views.get_sapi_by_id,name="get_sapi_by_id"),
    path("submit/edit/<int:item_id>",views.submit_sapi_form,name="submit_sapi_form"),
    path("delete/<int:item_id>",views.delete_sapi_by_id,name="delete_sapi_by_id"),
]