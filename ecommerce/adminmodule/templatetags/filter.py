from django import template
import datetime
register = template.Library()

@register.filter(name='split')
def split(value, key):
  """
    Returns the value turned into a list.
  """
  return value.split(key)

@register.filter(name='plus_days')
def plus_days(value,args):
    return value + datetime.timedelta(days=args)
   