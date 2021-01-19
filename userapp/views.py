from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from userapp.filter import ComputerFilterSet
from userapp.models import Computer
from userapp.pagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from userapp.serializer import ComputerModelSerializer
from userapp.throttle import MyThrottle


class UserAPIView(APIView):
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response("OK")

    def post(self, request):
        return Response("写操作")


class ComputerAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer


    # filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # search_fields = ["name", "price"]


    ordering = ["price"]


    # django-filter查询  通过filter_class指定过滤类
    filter_class = ComputerFilterSet


    pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination
