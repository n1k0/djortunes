import re
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import escape

register = template.Library()

@register.filter
@stringfilter
def fortunize(value):
    r = ""
    for line in value.splitlines():
        m = re.findall(r"^<(\w+)>\s?(.*)$", line.strip())
        if (len(m) > 0):
            for match in m:
                nick = match[0]
                quote = escape(match[1])
                r += "<dt>%s</dt><dd><q>%s</q></dd>\n" % (nick, quote)
        else:
            r += "<dt>&nbsp;</dt><dd>%s</dd>\n" % (line)
    return "<dl>%s</dl>" % r

