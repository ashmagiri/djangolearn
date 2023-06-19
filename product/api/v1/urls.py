from django.urls import path 
from .views import ProductView,ProductDetailView,ProductRestrictView

urlpatterns=[
    path('products/',ProductView.as_view()),
    path('product/<pk>/',ProductDetailView.as_view()),  #dynamic routing
    path('products-restrict/<pk>/',ProductRestrictView.as_view()),
]