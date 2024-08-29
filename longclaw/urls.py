from django.urls import include, re_path

from longclaw.basket import urls as basket_urls
from longclaw.checkout import urls as checkout_urls
from longclaw.shipping import urls as shipping_urls
from longclaw.orders import urls as order_urls

urlpatterns = [
    re_path(r'', include(basket_urls)),
    re_path(r'', include(checkout_urls)),
    re_path(r'', include(shipping_urls)),
    re_path(r'', include(order_urls)),
]
