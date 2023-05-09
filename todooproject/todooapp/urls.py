
from django.urls import path,include
from . import views


urlpatterns = [

    path('',views.add,name="add"),
    # path('details',views.details,name="details"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Detaillistview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.updatelist.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdelete.as_view(),name='cbvdelete')


]