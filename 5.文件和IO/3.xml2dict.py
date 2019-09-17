# -*- coding:utf-8 _*-
import xmltodict
from xml.parsers.expat import ExpatError


def xml2dict(content):
    try:
        if isinstance(content, str):
            dict_content = xmltodict.parse(content.decode("utf-8"))
        else:
            dict_content = xmltodict.parse(content)
    except ExpatError:
        return content

    return dict_content
