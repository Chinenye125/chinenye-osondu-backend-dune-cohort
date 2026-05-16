from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 6 # Default number of items per page
    page_size_query_param = 'page_size'  # Allow client to set page size with ?page_size=
    max_page_size = 50