from django.urls import re_path
from longclaw.shipping import api
from longclaw.settings import API_URL_PREFIX

address_list = api.AddressViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
address_detail = api.AddressViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    re_path(API_URL_PREFIX + r'addresses/$',
        address_list,
        name='longclaw_address_list'),
    re_path(API_URL_PREFIX + r'addresses/(?P<pk>[0-9]+)/$',
        address_detail,
        name='longclaw_address_detail'),
    re_path(API_URL_PREFIX + r'shipping/cost/$',
        api.shipping_cost,
        name='longclaw_shipping_cost'),
    re_path(API_URL_PREFIX + r'shipping/countries/$',
        api.shipping_countries,
        name='longclaw_shipping_countries'),
    re_path(API_URL_PREFIX + r'shipping/countries/(?P<country>[a-zA-Z]+)/$',
        api.shipping_options,
        name='longclaw_shipping_options'),
    re_path(API_URL_PREFIX + r'shipping/options/$',
        api.shipping_options,
        name='longclaw_applicable_shipping_rate_list')
]
