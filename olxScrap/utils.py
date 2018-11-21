import re
from w3lib.html import remove_tags
def clean(value):
  return remove_tags(value).strip()

def cleanDate(value):
  return re.search('[0-9]{1,2}( ){1}[a-z]+( ){1}[0-9]{4}', value, re.IGNORECASE).group(0)