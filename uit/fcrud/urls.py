from django.urls import path 
from .views import *
urlpatterns = [
    path('student-data', student_list, name='student-list'),
    path('student-add', student_add, name='student-add'),
    path('student-detail/<roll>', student_details, name='student-details'),
    path('student-edit/<roll>', student_edit, name='student-edit'),
    path('student-delete/<roll>', student_delete, name='student-delete'),

    #CBcrud
    path('list', StudentListView.as_view(), name='list'),
    path('create', StudentCreateView.as_view(), name='create'),
    path('update/<pk>', StudentUpdateView.as_view(), name='update'),
    path('delete/<pk>', StudentDeleteView.as_view(), name='delete'),
    path('detail/<pk>', StudentDetailView.as_view(template_name='CBcrud/detail.html'), name='detail'),
]