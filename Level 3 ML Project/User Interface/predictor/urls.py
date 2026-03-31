from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('house-price/', views.house_price, name='house_price'),
    path('loan-approver/', views.loan_approver, name='loan_approver'),
]
