def flatten(items):
   for item in items:
      if isinstance(item, list):
         yield from flatten(item)
      else:
         yield item

def relative_of(value, total):
   if total == 0:
      return 0
   else:
      return round((100.0 * value) / total, 2)
