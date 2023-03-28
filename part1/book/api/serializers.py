from ..models import Book
from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from django.utils.timezone import now


class BookSerializer(ModelSerializer):
    days_since_created = SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"
        # fields =
        # exclude =
        read_only_fields = ['id', 'created_date']

    def get_days_since_created(self, obj):
        return (now() - obj.created_date).days

    def validate(self, attrs):
        if attrs['name'] == attrs['description']:
            raise ValidationError(
                'İsim Alanı Açıklama Kısmı ile Aynı olamaz'
            )

        return attrs

    def validate_price(self, value):
        if value < 0:
            raise ValidationError(
                'Fiyat Negatif Değer içeremez'
            )
        return value
