from django.urls import path, include
from stocks.views import PlantsListCreateAPIView, PlantsRetrieveUpdateDestroyAPIView, OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('plants/', PlantsListCreateAPIView.as_view(), name="plants-list" ),
    path('plants/<int:pk>/', PlantsRetrieveUpdateDestroyAPIView.as_view(), name="plants-details" ),
    path('orders/', OrderListCreateAPIView.as_view(), name="order-list" ),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name="order-details" ),    
]


