from django.conf import settings
from django.urls import include
from django.urls import re_path
from django.contrib import admin

from search import views as search_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from longclaw import urls as longclaw_urls

urlpatterns = [
    re_path(r'^django-admin/', admin.site.urls),

    re_path(r'^admin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),

    re_path(r'^search/$', search_views.search, name='search'),

    re_path(r'', include(longclaw_urls)),
    re_path(r'', include(wagtail_urls))
]


if settings.DEBUG:
    from django.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
