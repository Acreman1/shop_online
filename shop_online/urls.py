import xadmin
# from django.conf.urls import url,include
from django.urls import path,include
from django.views.static import serve
from shop_online.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet,CategoryViewSet,BannerViewSet,HotSearchsViewset,IndexCategoryViewset
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SmsCodeViewset,UserViewSet
from user_operation.views import UserFavViewSet,LeavingMessageViewset,AddressViewSet
from trade.views import ShoppingCartViewSet,OrderViewSet,AlipayView

router = DefaultRouter()

router.register(r'goods',GoodsListViewSet)
router.register(r'categorys',CategoryViewSet,basename='categorys')
router.register(r'code',SmsCodeViewset,basename='code')
router.register('users',UserViewSet,basename="users")
router.register(r'userfavs',UserFavViewSet,basename="userfavs")
router.register(r'messages',LeavingMessageViewset,basename='messages')
router.register(r'address', AddressViewSet,basename='address')
router.register(r'shopcarts',ShoppingCartViewSet,basename="shopcarts")
router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'banners', BannerViewSet, basename="banners")
router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")
router.register(r'hotsearchs', HotSearchsViewset, basename="hotsearchs")


schema_view = get_schema_view(title='corejson')

urlpatterns = [
    # url('xadmin/', xadmin.site.urls),
    # url('ueditor/', include('DjangoUeditor.urls')),
    # # 上传图片得路径
    # url('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # url('api-auth/',include('rest_framework.urls')),
    # url('',include(router.urls)),
    # url('docs/',include_docs_urls(title='DRF文档')),
    # url('schema/',schema_view)
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 上传图片得路径
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('api-auth/',include('rest_framework.urls')),
    path('',include(router.urls)),
    path('api-token-auth',views.obtain_auth_token),
    path('login/',obtain_jwt_token),
    path('docs/',include_docs_urls(title='DRF文档')),
    path('schema/',schema_view),
    path('alipay/return/',AlipayView.as_view()),
    path('',include('social_django.urls',namespace='social'))
]
