# Django
from django.http import HttpResponse
from django.http import Http404
# models
from redirects.models import Redirect

# Utilites
import json


def get_url(request, key):
    """This view receives a key and returns the associated url"""

    data = Redirect.get_redirect(key)
    if data is None:
        raise Http404(
            "There is no redirect with this key '{}' you may try with  another key: ".format(key))

    return HttpResponse(
        json.dumps(data),
        content_type='application/json'
    )
