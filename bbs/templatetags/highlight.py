import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='highlight')
@stringfilter
def highlight(value, keyword, color="red"):
    _keyword = re.compile(re.escape(keyword), re.IGNORECASE)
    _val = _keyword.sub("<span style='color:%s'>%s</span>" %(color, keyword), value)

    return mark_safe(_val)