from rest_framework import serializers
from .models import *


class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableNumbers
        fields = ('number', 'order', 'price_dollar', 'delivery_data', 'price_rub')