# -*- coding:utf-8 _*-
def dict2xml(data):
    xml_data = []
    for key, value in data.items():
        if isinstance(value, dict):
            xml_str = dict2xml(value)
            s = "<{key}>{value}</{key}>".format(key=key, value=xml_str)
        elif isinstance(value, list):
            s = ""
            for dic in value:
                xml_str = dict2xml(dic)
                s += "<{key}>{value}</{key}>".format(key=key, value=xml_str)
        elif value is None:
            s = "<{key}></{key}>".format(key=key)
        else:
            s = "<{key}>{value}</{key}>".format(key=key, value=value)
        xml_data.append(s)
    return ''.join(xml_data)

