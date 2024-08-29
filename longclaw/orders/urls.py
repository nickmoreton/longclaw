from django.urls import re_path

from longclaw.orders import api
from longclaw.settings import API_URL_PREFIX

orders = api.OrderViewSet.as_view({
    'get': 'retrieve'
})

fulfill_order = api.OrderViewSet.as_view({
    'post': 'fulfill_order'
})

refund_order = api.OrderViewSet.as_view({
    'post': 'refund_order'
})

PREFIX = r'^{}order/'.format(API_URL_PREFIX)
urlpatterns = [
    re_path(
        PREFIX + r'(?P<pk>[0-9]+)/$',
        orders,
        name='longclaw_orders'
    ),

    re_path(
        PREFIX + r'(?P<pk>[0-9]+)/fulfill/$',
        fulfill_order,
        name='longclaw_fulfill_order'
    ),

    re_path(
        PREFIX + r'(?P<pk>[0-9]+)/refund/$',
        refund_order,
        name='longclaw_refund_order'
    )
]
