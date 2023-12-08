from django.db import models

class Author(models.Model):

	name = models.CharField(max_length = 50)
	date = models.DateField(auto_now_add = True)
	def __str__(self):
		return self.name
	
class Book(models.Model):
	title = models.CharField(max_length = 20)
	author = models.ForeignKey(Author,on_delete =models.CASCADE)
	is_active = models.BooleanField(default=True)
	isbn = models.CharField(max_length=13,unique=True,default= '0000000000000')
	def __str__(self):
		return self.title
class Review(models.Model):
	review_book = models.ForeignKey(Book,on_delete= models.CASCADE)
	comment = models.CharField(max_length=300)
	