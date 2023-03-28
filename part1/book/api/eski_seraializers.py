from rest_framework import serializers
from ..models import Book
from rest_framework.validators import UniqueValidator


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    created_date = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    def validate(self, attrs):
        if attrs['name'] == attrs['description']:
            raise serializers.ValidationError(
                'İsim Alanı Açıklama Kısmı ile Aynı olamaz'
            )

        return attrs

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'Fiyat Negatif Değer içeremez'
            )
        return value
