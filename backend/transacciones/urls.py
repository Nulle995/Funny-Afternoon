from django.urls import path
from .views import (
    TransaccionListCreateAPIView,
    TransaccionUpdateAPIView,
    TransaccionDeleteAPIView,
    InformeMensualView,
)

urlpatterns = [
    path("", TransaccionListCreateAPIView.as_view(), name="transacciones"),
    path(
        "<int:pk>/update/",
        TransaccionUpdateAPIView.as_view(),
        name="transaccion-update",
    ),
    path(
        "<int:pk>/delete/",
        TransaccionDeleteAPIView.as_view(),
        name="transaccion-delete",
    ),
    path("informe/mensual/", InformeMensualView.as_view(), name="informe-mensual"),
]
