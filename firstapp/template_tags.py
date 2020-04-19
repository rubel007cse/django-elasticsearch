from django.template.defaulttags import register
import ast

@register.filter
def get_item(dictionary, key):

    dicts = ast.literal_eval(dictionary)
    return dicts.get(key)