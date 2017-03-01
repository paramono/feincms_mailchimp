# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from feincms_mailchimp.urls import urlpatterns as feincms_mailchimp_urls

urlpatterns = [
    url(r'^', include(feincms_mailchimp_urls, namespace='feincms_mailchimp')),
]
