# -*- coding:utf-8 _*-
from xml.etree.ElementTree import Element, tostring


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {"name": "Python教程", "price": 22.5, "date": ""}
print(tostring(dict_to_xml("book", s)))  # <book><name>Python&#25945;&#31243;</name><price>22.5</price><date /></book>
