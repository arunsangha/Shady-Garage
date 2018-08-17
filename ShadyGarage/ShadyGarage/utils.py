import random
import string

from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars)for _ in range(size))

def unique_order_id_generator(instance):
    order_id = random_string_generator()

    class_ = instance.__class__
    qs_exists = class_.objects.filter(order_id=order_id).exists()

    if qs_exists:
        return random_string_generator(instance)
        
    return order_id
