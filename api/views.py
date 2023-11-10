from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from .models import Book
from .serializers import BookSerializer, ForList


# Create your views here.


class TenReqPerMin(UserRateThrottle):
    rate = '10/min'


class ThreeReqPerMin(UserRateThrottle):
    rate = '3/min'


class AvailableBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ForList
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # throttle_classes = [TenReqPerMin]

    def get_queryset(self):
        return Book.objects.all().filter(is_available=True)


class AllBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ForList
    permission_classes = [AllowAny]
    # throttle_classes = [TenReqPerMin]


class CreateBook(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # throttle_classes = [ThreeReqPerMin]


class DetailBook(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # throttle_classes = [TenReqPerMin]


class UpdateBook(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # throttle_classes = [ThreeReqPerMin]


class DeleteBook(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # throttle_classes = [ThreeReqPerMin]


class ReturnBookByOwner(ListAPIView):
    queryset = Book
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # throttle_classes = [TenReqPerMin]

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(user=user)


class SortByField(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'category', 'ISO', 'about_book', 'published']
    search_fields = ['title']
    permission_classes = [AllowAny]
    # throttle_classes = [TenReqPerMin]


class SearchByTitle(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [AllowAny]
    # throttle_classes = [TenReqPerMin]
