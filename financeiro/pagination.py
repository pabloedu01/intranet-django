from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_description = 'page'