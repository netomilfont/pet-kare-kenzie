from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 2
    page_query_param = 'trait'