from django.urls import path
from .views import user, useraccountActivate

urlpatterns = [
    path('show/',user),
    path('activate/<uid>/<token>/',useraccountActivate, name='activate')
]