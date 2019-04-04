__author__ = 'bsetzer'

import datetime
import re
import json

# based on http://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable-in-python
# answer by fiatjaf


def date_default(obj):
    if type(obj) is datetime.date or type(obj) is datetime.datetime:
        # return obj.isoformat()
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    else:
        raise TypeError

# based on http://stackoverflow.com/questions/8793448/how-to-convert-to-a-python-datetime-object-with-json-loads
# answer by Nicola Iarocci
# this version does not ignore exceptions


def date_hook(dct):
    for k, v in dct.items():
        if isinstance(v, str) and re.fullmatch(r"\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d", v):
            # print('date-time match: ', v)
            dct[k] = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
            # print('converted to: ', dct[k])
    return dct


def dumps(obj, **kwargs):
    return json.dumps(obj, default=date_default, **kwargs)
    # return json.dumps(obj, **kwargs)


def loads(jsn, **kwargs):
    return json.loads(jsn, object_hook=date_hook, **kwargs)
