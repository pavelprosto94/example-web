import urllib3

def speak():
  http = urllib3.PoolManager()
  try:
    source = http.request('GET', 'http://webcode.me')
  except Exception as e:
    return str(e)
  else:
    html_str = source.data.decode('utf-8')
    return html_str