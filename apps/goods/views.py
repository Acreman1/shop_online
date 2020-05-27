from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets,filters
from goods.serializers import GoodsSerializer, IndexCategorySerializer, HotWordsSerializer
from .models import Goods, GoodsCategory, Banner, HotSearchWords
from .filter import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import GoodsSerializer,CategorySerializer,BannerSerializer
from rest_framework.pagination import PageNumberPagination


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# class GoodsListView(APIView):
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods,many=True)
#         return Response(goods_serializer.data)


# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    # 设置筛选
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = GoodsFilter

    # 设置搜索
    search_fields = ('name','goods_brief','goods_desc')
    # 排序
    ordering_fields = ['sold_num','add_time']


class CategoryViewSet(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BannerViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    首页轮播列表
    """
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["蔬菜水果", "酒水饮料"])
    serializer_class = IndexCategorySerializer


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer