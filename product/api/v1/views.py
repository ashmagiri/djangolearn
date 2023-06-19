from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from .serializers import ProductSerializer
from product.models import Product
from rest_framework.permissions import IsAuthenticated 

class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    
    def put(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)
    
    
    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)
    
    def delete(self,request,*args,**kwargs):
        pid=self.request.query_params.get("pid")
        product=Product.objects.filter(id=pid).delete()
        return Response({"message":"product deleted successfully"})
    
    
class ProductDetailView(RetrieveAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class ProductRestrictView(RetrieveAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    permission_classes=[IsAuthenticated,]