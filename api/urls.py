from django.urls import path
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('', views.AvailableBooks.as_view(), name='available_books'),
    path('sort/', views.SortByField.as_view(), name='sort'),
    path('search/', views.SearchByTitle.as_view(), name='search'),
    path('all', views.AllBooks.as_view(), name='all_books'),
    path('new', views.CreateBook.as_view(), name='new'),
    path('<int:id>', views.DetailBook.as_view(), name='detail'),
    path('<int:id>/delete', views.DeleteBook.as_view(), name='delete'),
    path('<int:id>/update', views.UpdateBook.as_view(), name='update'),
    path('<str:username>', views.ReturnBookByOwner.as_view(), name='return_book_by_owns'),
    path('swagger-ui/', TemplateView.as_view(template_name='api/swagger-ui.html', extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),
]
