from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets
from goods.serializers import GoodsSerializer
from .models import Goods


# class GoodsListView(APIView):
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods,many=True)
#         return Response(goods_serializer.data)


# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # pagination_class = GoodsPagination