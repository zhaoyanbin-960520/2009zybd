from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination



class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 5


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 5


class MyCursorPagination(CursorPagination):
    page_size = 3
    cursor_query_param = "cursor"
    max_page_size = 5
    ordering = "-price"
