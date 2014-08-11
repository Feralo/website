import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown.markdown(str(value), ["nl2br", ], safe_mode=True, enable_attributes=False))


# Considered an api http://stackoverflow.com/a/23032089
# modified a solution: http://matthewdaly.co.uk/blog/2014/01/02/django-blog-tutorial-the-next-generation-part-2/
#   to get it to work with python3
#   safe will remove html: http://stackoverflow.com/a/13520697
#   force_unicode doesn't exist in python3 https://code.djangoproject.com/ticket/18772