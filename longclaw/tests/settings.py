# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

import os

from wagtail import VERSION as WAGTAIL_VERSION

DEBUG = True
# USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "longclaw.tests.urls"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail" if WAGTAIL_VERSION >= (3, 0) else "wagtail.wagtailcore",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.settings",
    "modelcluster",
    "taggit",
    "rest_framework",
    "django_extensions",
    "longclaw.core",
    "longclaw.configuration",
    "longclaw.shipping",
    "longclaw.products",
    "longclaw.orders",
    "longclaw.checkout",
    "longclaw.basket",
    "longclaw.stats",
    "longclaw.contrib.productrequests",
    "longclaw.tests.testproducts",
    "longclaw.tests.trivialrates",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "wagtail.contrib.legacy.sitemiddleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(os.path.dirname(__file__), "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "longclaw.configuration.context_processors.currency",
            ],
        },
    },
]

STATIC_URL = "/static/"

PRODUCT_VARIANT_MODEL = "testproducts.ProductVariant"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
