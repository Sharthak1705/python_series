from django.urls import path
from . import views

#localhost:8000/chai/

urlpatterns = [
    path('', views.all_chai, name='all_home'),
    # path('orders/',views.order, name='order'),

]
