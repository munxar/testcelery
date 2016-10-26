from django.db.models.signals import post_save
from tasks import async_task


def post_save_product(sender, **kwargs):
    # send the products id
    # if we need 100% consistency, then we have to serialize the object here and send that.
    # benefit of just id is the reduced data + delayed serialization.
    # choose your poison ;-)
    async_task.delay(kwargs['instance'].id)


def register_signals():
    # call post_save_product after a successful save
    post_save.connect(receiver=post_save_product, sender='async.Product')
