from rest_framework import permissions
from rest_framework.views import APIView

from Bookstore.settings import EMAIL_HOST_USER

from api.views import ThreeReqPerMin
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.generics import CreateAPIView
from django.core.mail import send_mail


from .models import BlogPostSubscription
from .serializers import LoginSerializer, SignupSerializer, BlogPostSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    # throttle_classes = [ThreeReqPerMin]

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response('Muvafaqiiyatli otdingiz')


class Signup(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
    # throttle_classes = [ThreeReqPerMin]


Email = str


class Subscribe(APIView):
    queryset = BlogPostSubscription.objects.all()
    serializer_class = BlogPostSerializer

    def post(self, request):
        global Email
        serializer = BlogPostSerializer(data=request.data)
        response = BlogPostSerializer(data=request.data.get('email'))
        Email = response.initial_data
        to_mail = [Email]
        send_mail('Welcome New Subscriber',
                  'Assalomu alaykum xurmatli mijoz, siz bizni blog postlarimizga obuna bo’ldingiz va tez orada biz sizga eng yaxshi postlarimizni yuboramiz',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_mail,
                  fail_silently=False
                  )
        print(f'Message sent to {Email}')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
