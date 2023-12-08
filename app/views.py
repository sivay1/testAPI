from django.shortcuts import render

from .models import Author,Book,Review
from .serializers import BookSerializer,AuthorSerializer,ReviewSerializer
from rest_framework import generics
class AuthorView(generics.ListCreateAPIView):

	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
class SingleAuthView(generics.RetrieveUpdateDestroyAPIView):

	queryset = Author.objects.all()
	serializer_class = AuthorSerializer

class BookView(generics.ListCreateAPIView):
	
	queryset = Book.objects.all().order_by('title')
	serializer_class = BookSerializer
	ordering_fields = ['title']
	filterset_fields = ['title']
	search_fields = ['isbn']

class SingleBookView(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
class SingleBookEditView(generics.RetrieveUpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class ReviewView(generics.ListCreateAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	

class ViewBooks(generics.ListAPIView):
	queryset = Book.objects.filter(is_active=True).order_by('title')
	serializer_class = BookSerializer
	ordering_fields = ['title']
	filterset_fields = ['title']
	search_fields = ['isbn']

class BookDestroyView(generics.RetrieveDestroyAPIView):
	queryset = Book.objects.filter(is_active=True)
	serializer_class = BookSerializer
	def perform_destroy(self, instance):
		instance.is_active = False
		instance.save()