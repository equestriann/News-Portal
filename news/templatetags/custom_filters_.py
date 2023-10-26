from django import template

register = template.Library()

explicit = [
    'версий',
    'угнетения',
]

@register.filter()
def censor(value):
    new_value = value
    for word in explicit:
        new_value = new_value.replace(word, word[:1] + '*' * (len(word) - 1))
    return new_value
