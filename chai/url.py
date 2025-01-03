from django.urls import path
from . import views

#localhost:8000/chai/

urlpatterns = [
    path('', views.all_chai, name='all_home'),
    path('<int:chai_id>/', views.chai_detail,name='chai_detail'),
    path('chai_store/', views.chai_store, name ='chai_store')
    # path('orders/',views.order, name='order'),


]
