from django.views.generic.base import View

from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        """
            通过django得view实现商品列表页
        """
        json_list = []
        goods = Goods.objects.all()
        for i in goods:
            json_dict = {}
            json_dict['name'] = i.name
            json_dict['category'] = i.category.name
            json_dict['market_price'] = i.market_price
            json_list.append(json_dict)
        """
            model_to_dict
        """
        # from django.forms.models import model_to_dict
        # for i in goods:
        #     json_dict = model_to_dict(i)
        #     json_list.append(json_dict)
        """
            django serializer
        """
        # from django.core import serializers
        # from django.http import JsonResponse
        # import json
        # json_data = serializers.serialize('json',goods)
        # json_data = JsonResponse(json_data)
        # return JsonResponse(json_data,safe=False)

        from django.http import HttpResponse
        # 只能转换dict和list类型
        import json
        # 返回数据，指定类型
        return HttpResponse(json.dumps(json_list),content_type="application/json")