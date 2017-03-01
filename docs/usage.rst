=====
Usage
=====

To use feincms_mailchimp in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'feincms_mailchimp.apps.FeincmsMailchimpConfig',
        ...
    )

Add feincms_mailchimp's URL patterns:

.. code-block:: python

    from feincms_mailchimp import urls as feincms_mailchimp_urls


    urlpatterns = [
        ...
        url(r'^', include(feincms_mailchimp_urls)),
        ...
    ]
