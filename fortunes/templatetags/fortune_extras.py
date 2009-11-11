import re
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import escape

register = template.Library()

@register.filter
@stringfilter
def fortunize(value):
    """
    Transforms a fortune plain text into htmlized (but safe) one.
    """
    r = ""
    for i, line in enumerate(value.splitlines()):
        m = re.findall(r"^<(\w+)>\s?(.*)$", line.strip())
        className = "odd" if i % 2 == 0 else "even"
        if (len(m) > 0):
            for match in m:
                nick = match[0]
                quote = escape(match[1])
                r += "<dt class=\"%s\">%s</dt><dd><q>%s</q></dd>\n" % (className, nick, quote)
        else:
            r += "<dt>&nbsp;</dt><dd>%s</dd>\n" % (line)
    return "<dl>%s</dl>" % r

