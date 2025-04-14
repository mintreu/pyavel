# vedix/utils/stub_loader.py

import os

def render_stub(stub_name, context):
    path = os.path.join("vedix", "Stubs", stub_name)
    with open(path) as f:
        template = f.read()
    for key, val in context.items():
        template = template.replace("{{ " + key + " }}", val)
    return template
