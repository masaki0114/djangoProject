from django_filters import filters
from django_filters import FilterSet
from .models import Item

class MyOrderingFilter(filters.OrderingFilter):
    """docstring for MyOrderingFilter"""
    descending_fmt = '%s (降順)'

class ItemFilter(FilterSet):
    """docstring for ItemFilter"""
    name = filters.CharFilter(label='氏名', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields = (
            ('name', 'name'),
            ('age', 'age'),
        ),
        field_labels = {
            'name':'氏名',
            'age':'年齢',
        },
        label = '並び順'
    )

    class Meta:
        """docstring for Meta"""
        model = Item
        fields = ('name', 'sex', 'memo')