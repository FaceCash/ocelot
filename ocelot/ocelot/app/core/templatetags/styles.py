from django import template

register = template.Library()

class isCurrentNode(template.Node):
    def __init__(self, patterns):
        self.patterns = patterns
    def render(self, context):
        path = context['request'].path
        for pattern in self.patterns:
            curr_pattern = template.Variable(pattern).resolve(context)
            if path == curr_pattern:
                return "active"
        return ""

@register.tag
def is_current(parser, token):
    """ Check if the browse is currently at this supplied url"""
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError, "%r tag requires at least one argument" % args[0]
    return isCurrentNode(args[1:])