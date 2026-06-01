from rest_framework.pagination import LimitOffsetPagination


class PostPagination(LimitOffsetPagination):
    """Пагинация только при передаче параметра limit в запросе."""

    def paginate_queryset(self, queryset, request, view=None):
        if 'limit' not in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view)
