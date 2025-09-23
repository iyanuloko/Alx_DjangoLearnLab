from rest_framework import serializers
from .models import Author, Book
from datetime import datetime
# book serializer for the Book model for all fields
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# author serializer for name and nested book serializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
       fields = ['name, books']
# validation function to prevent publication date from being set to the future
    def validate(self, data):
        if data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("publication_year must be before current year")
        return data