from django.urls import path
from app import views

urlpatterns = [
	path('author/',views.AuthorView.as_view()),
	path('author/<int:pk>',views.SingleAuthView.as_view()),
	path('book/',views.BookView.as_view(),name = 'book'), #lists all books with inactve status false as well
	path('book/<int:pk>',views.SingleBookView.as_view(),name = 'single-book'),
	path('reviews/',views.ReviewView.as_view(),name = 'review'),
	path('view-books/',views.ViewBooks.as_view(),name = 'view-book'), #view all books with true is_active value 
	path('update-book/<int:pk>',views.SingleBookEditView.as_view(),name = 'update'), #users can goto update-book/1 or 2 to go to a single book record and can edit
	path('delete-book/<int:pk>',views.BookDestroyView.as_view(),name = 'delete'), # delete single book record

]

