from django.urls import path
from . import views

urlpatterns = [
    path('allsandt/', views.sandt_list, name='sandt_list'),
    path('registration/', views.sandt_regi, name='sandt_regi'),
    path('edit/<int:pk>', views.edit_sandt, name='edit_sandt'),
    path('delete/<int:sandt_id>', views.delete_sandt, name='delete_sandt'),
]

