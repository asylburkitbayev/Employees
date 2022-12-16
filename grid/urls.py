from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('addnew', views.add_new),
    path('edit/<id>', views.edit),
    path('update/<id>', views.update),
    path('delete/<id>', views.destroy),
    path('detail/<id>', views.detail, name='detail')
]
