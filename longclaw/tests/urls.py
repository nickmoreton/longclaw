# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.urls import include
from django.urls import re_path

from wagtail.admin import urls as admin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as documents_urls
from longclaw import urls as longclaw_urls
from longclaw.contrib.productrequests import urls as request_urls

urlpatterns = [
    re_path(r'^admin/', include(admin_urls)),
    re_path(r'^documents/', include(documents_urls)),

    re_path(r'', include(longclaw_urls)),
    re_path(r'', include(request_urls)),
    re_path(r'', include(wagtail_urls)),


]
