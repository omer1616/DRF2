from ..models import Book, Author
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from django.utils.timezone import now


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = "__all__"
        # fields =
        # exclude =
        read_only_fields = ['id', 'created_date']

    def get_days_since_created(self, obj):
        return (now() - obj.created_date).days

    def get_author_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

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


class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)
    books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="book-detail")

    class Meta:
        model = Author
        fields = "__all__"
