import xadmin
from django.conf.urls import url,include
from django.views.static import serve
from shop_online.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'good',GoodsListViewSet)

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('ueditor/', include('DjangoUeditor.urls')),
    # 上传图片得路径
    url('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    url('api-auth/',include('rest_framework.urls')),
    url('',include(router.urls)),
    url('docs/',include_docs_urls(title='DRF文档')),
]
