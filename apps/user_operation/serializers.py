import re

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from goods.serializers import GoodsSerializer
from shop_online.settings import REGEX_MOBILE
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]
        model = UserFav
        fields = ("user", "goods", "id")


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class LeavingMessageSerializer(serializers.ModelSerializer):
    """
        用户留言
    """
    # 获取当前登录用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # read_only=True,实现只返回不提交,不需要自己添加时间,format格式化时间
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")

    class Meta:
        model = UserLeavingMessage
        fields = ("user", "message_type", "subject", "message", "file", "id", "add_time")


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "address", "signer_name", "add_time", "signer_mobile")

    def validate_signer_mobile(self, signer_mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 验证手机号码是否合法
        if not signer_mobile:
            raise serializers.ValidationError("请输入手机号码")
        if not re.match(REGEX_MOBILE, signer_mobile):
            raise serializers.ValidationError("手机号码非法")
        return signer_mobile

    def validate_signer_name(self, signer_name):
        """
        验证签收人
        :param data:
        :return:
        """
        # 验证签收人是否合法
        if not signer_name:
            raise serializers.ValidationError("请输入签收人")

        return signer_name

    def validate_address(self, address):
        """
        验证详细地址
        :param data:
        :return:
        """
        # 验证详细地址是否合法
        if not address:
            raise serializers.ValidationError("请输入详细地址")

        return address