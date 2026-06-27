from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Producto
from .serializers import ProductSerializer, DesactivateProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer

class DesactivateProductView(APIView):

    def put(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response(
                {"detail": "Producto no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        producto.status = False
        producto.save()

        return Response(
            {"message": "Producto desactivado correctamente."},
            status=status.HTTP_200_OK
        )
