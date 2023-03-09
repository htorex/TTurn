from django import template

register = template.library()

@register.filter()
def horario_format(value):
    return 'Hora{}'.format(value)
