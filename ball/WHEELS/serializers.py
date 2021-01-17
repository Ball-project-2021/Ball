from rest_framework import serializers

from .models import Wheel


class WheelListSerializer(serializers.ModelSerializer):
    car_model = serializers.SlugRelatedField(slug_field="model_name", read_only=True)
    brand = serializers.SlugRelatedField(slug_field="brand_name", read_only=True)
    product_year = serializers.SlugRelatedField(slug_field="product_year", read_only=True)

    class Meta:
        model = Wheel
        fields = ('id', 'brand', 'car_model', 'vin_code', 'price', 'product_year')


class WheelDetailSerializer(serializers.ModelSerializer):
    car_model = serializers.SlugRelatedField(slug_field="model_name", read_only=True)
    brand = serializers.SlugRelatedField(slug_field="brand_name", read_only=True)
    country = serializers.SlugRelatedField(slug_field="country_name", read_only=True)
    region_name = serializers.SlugRelatedField(slug_field="region_name", read_only=True)
    region_child = serializers.SlugRelatedField(slug_field="region_child", read_only=True)
    man_country = serializers.SlugRelatedField(slug_field="man_country", read_only=True)
    product_year = serializers.SlugRelatedField(slug_field="product_year", read_only=True)
    clearance = serializers.SlugRelatedField(slug_field="clearance", read_only=True)
    color = serializers.SlugRelatedField(slug_field="color", read_only=True)

    class Meta:
        model = Wheel
        fields = '__all__'
