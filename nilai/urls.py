from django.urls import path
from . import views

urlpatterns = [
    # nilai
    path("",views.index_nilai,name="nilai"),
    path("submit-nilai",views.submit_nilai_form,name="submit_nilai_form"),
    path("daftar-nilai",views.get_all_nilai,name="get_all_nilai"),
    path("edit-nilai/<int:item_id>",views.get_nilai_by_id,name="get_nilai_by_id"),
    path("submit-nilai/<int:item_id>/",views.submit_nilai_form,name="submit_nilai_form"),
    path("delete-nilai/<int:item_id>/",views.delete_nilai_by_id,name="delete_nilai_by_id"),

    # parameter
    path("input-parameter",views.index_parameter,name="parameter"),
    path("submit-parameter",views.submit_parameter_form,name="submit_parameter_form"),
    path("daftar-parameter",views.get_all_parameter,name="get_all_parameter"),
    path("edit-parameter/<int:item_id>",views.get_parameter_by_id,name="get_parameter_by_id"),
    path("submit-parameter/<int:item_id>/",views.submit_parameter_form,name="submit_parameter_form"),
    path("delete-paramter/<int:item_id>/",views.delete_parameter_by_id,name="delete_parameter_by_id"),
]
