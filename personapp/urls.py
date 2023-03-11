
from django.urls import path
from . import views
urlpatterns = [
    path('', views.person_list),
    path('Add/', views.AddPerson),
    path('Edit/<id>', views.EditPerson),
    path('Delete/<eid>', views.DeletePerson),
    path('View/<eid>', views.ViewPerson),
]
