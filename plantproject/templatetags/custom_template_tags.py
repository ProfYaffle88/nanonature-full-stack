from django import template
import cloudinary

register = template.Library()

@register.filter
def cloudinary_transform(image_url):
    # Cloudinary transformation parameters
    width = 'auto'  # Example maximum width
    quality = 'auto:low'
    format = 'auto'

    # Generate Cloudinary URL with transformations
    return cloudinary.utils.cloudinary_url(image_url, width=width, quality=quality, format=format)[0]
