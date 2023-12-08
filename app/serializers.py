from rest_framework import serializers

from .models import Author,Book,Review

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Review
		fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
	# author = AuthorSerializer()
	author_name = serializers.SerializerMethodField()
	reviews = ReviewSerializer(many=True , read_only=True)
	class Meta:
		model = Book
		fields = '__all__'
	def get_author_name(self,n):
		return n.author.name

class ViewBookserializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'
