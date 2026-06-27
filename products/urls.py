from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailView,
)

urlpatterns = [
    path(
        "",
        ProductListCreateView.as_view(),
        name="products"
    ),

    path(
        "<int:pk>/",
        ProductDetailView.as_view(),
        name="product"
    ),

    path(
        "desactive/<int:pk>/",
        DesactivateProductView.as_view(),
        name="desactive-product"
    ),
]
