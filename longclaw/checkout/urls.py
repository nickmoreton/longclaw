from django.urls import re_path

from longclaw.checkout import api, views
from longclaw.settings import API_URL_PREFIX

urlpatterns = [
    re_path(API_URL_PREFIX + r'checkout/$',
        api.capture_payment,
        name='longclaw_checkout'),
    re_path(API_URL_PREFIX + r'checkout/prepaid/$',
        api.create_order_with_token,
        name='longclaw_checkout_prepaid'),
    re_path(API_URL_PREFIX + r'checkout/token/$',
        api.create_token,
        name='longclaw_checkout_token'),
    re_path(r'checkout/$',
        views.CheckoutView.as_view(),
        name='longclaw_checkout_view'),
    re_path(r'checkout/success/(?P<pk>[0-9]+)/$',
        views.checkout_success,
        name='longclaw_checkout_success')
]
