import random
import string

from django.utils.text import slugify
from PIL import Image, ExifTags


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars)for _ in range(size))

def unique_order_id_generator(instance):
    order_id = random_string_generator()

    class_ = instance.__class__
    qs_exists = class_.objects.filter(order_id=order_id).exists()

    if qs_exists:
        return random_string_generator(instance)

    return order_id



def rotate_image(filepath):
  try:
    image = Image.open(filepath)
    for orientation in ExifTags.TAGS.keys():
      if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    image.save(filepath)
    image.close()
  except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass
