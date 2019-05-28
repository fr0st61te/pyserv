# -*- coding: utf8 -*-
from xml.dom.minidom import Document
from server.const import Types
import xml.parsers.expat
import unittest


def parse_rsp(data):
    dictdata = {}
    def start_element(name, attrs):
        type = None
        if 't' in attrs:
            type = Types.types[attrs['t']]
            del attrs['t']
        else:
            type = int

        for key, value in attrs.items():
            dictdata[key] = type(value)

    def end_element(name):
        pass

    def char_data(data):
        pass

    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = start_element
    p.CharacterDataHandler = char_data
    p.EndElementHandler = end_element
    try:
        p.Parse(data)
    except xml.parsers.expat.ExpatError:
        return dictdata
    return dictdata


def create_rsp(data, id):
    # Create the minidom document
    doc = Document()
    answer = doc.createElement('rsp')
    answer.setAttribute('id', str(id))

    doc.appendChild(answer)

    for key, value in data.items():
        param = doc.createElement('p')
        param.setAttribute(str(key), str(value))
        param.setAttribute('t', Types.types[type(value)])
        answer.appendChild(param)
    # 23 symbols - this is <?xml version="1.0" ?>
    return str(doc.toxml()[22:]) + str("\x00")


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.data = {
            'token': 'abcdefgh',
            'server': '192.168.10.10:500'
        }

        self.text = """
        <cmd id="0">
            <ps archive="0">
                <p login="abcde" t="c" />
                <p password="abcde" t="c" />
            </ps>
        </cmd>
        """

    def testsample1(self):
        data = create_rsp(self.data, 1)
        print(data)

    def testsample2(self):
        data = parse_rsp(self.text)
        print(data)


if __name__ == '__main__':
    unittest.main()
