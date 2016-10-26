from django.core.serializers import json
from async.models import Product, ProductJson
from django.forms.models import model_to_dict
from celery_app import app
import json


@app.task(name="export")
def async_task(product_id):

    # get product by primary key
    product = Product.objects.get(pk=product_id)

    # extract related product json
    if hasattr(product, 'product_json'):
        product_json = product.product_json
    else:
        # create new product json
        product_json = ProductJson(product=product, data="{}")

    # assuming obj is your model instance
    dict_obj = model_to_dict(product)

    # update json data
    product_json.data = json.dumps(dict_obj)

    # put json into queue
    # NOT IMPLEMENTED <- add this in real implementation

    # save product json
    product_json.save()


