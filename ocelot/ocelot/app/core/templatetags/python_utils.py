from django import template

register = template.Library()

class RenameNode( template.Node ):
    def __init__( self, fromvar, tovar ):
        self.fromvar = fromvar; self.tovar = tovar
    def render( self, context ):
        context[self.tovar] = self.fromvar
        # very important: don't forget to return a string!!
        return ''
@register.tag
def rename( parser, token ):
    tokens = token.contents.split()
    if len( tokens ) != 3:
        raise template.TemplateSyntaxError, \
              "'%s' tag takes two arguments" % tokens[0]
    return RenameNode( tokens[1], tokens[2] )