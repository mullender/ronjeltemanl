import json
from string import Template

with open('content.json', 'r') as f:
    decoder = json.JSONDecoder(object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=False)
    j = decoder.decode(f.read())

with open('index.template.html', 'r') as f:
    s = Template(f.read())
    for page in j:
        with open('public/'+page['url'], 'w') as out:
            out.write(s.substitute(page))