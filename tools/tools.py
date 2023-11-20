import os

from oc_lettings_site import settings


def read_sql(app, filename):
    filepath = os.path.join(settings.BASE_DIR, app, 'sql', filename)
    with open(filepath, 'rb') as f:
        s = f.read()
    return s
