from django.urls import path

from classapp import views

app_name='classapp'
urlpatterns=[
    path('classmates/',views.classmates,name='classmates'),
    path('add/',views.add,name='add'),
    path('addMate/',views.addMate,name='addMate'),
    path('delMate/',views.delMate,name='delMate'),
    path('update/',views.update,name='update'),
    path('update_mate_node/',views.update_mate_node,name='update_mate_node'),
    path('class_mate_node/',views.class_mate_node,name='class_mate_node'),
]