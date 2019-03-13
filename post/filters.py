from django.contrib.auth import get_user_model
from django.db.models import Count
from django_filters import rest_framework as filters

User = get_user_model()


class UserFilter(filters.FilterSet):
    order_by = filters.CharFilter(method='filter_order_by')

    def filter_order_by(self, queryset, _, value):
        if value == 'post':
            return queryset.annotate(count_posts=Count('post')).order_by('-count_posts')
        return queryset
