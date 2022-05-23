# -*- coding: utf-8 -*-
# mypy: ignore-errors

import argparse
from io import open

parser = argparse.ArgumentParser()
parser.add_argument('document')
parser.add_argument('name')

arguments = parser.parse_args()
document = arguments.document
name = arguments.name

try:
    with open(document, 'r+', encoding='utf-8') as file:
        content = file.read()
except:
    print('Error while opening file')
    exit(2)

document_lines = content.splitlines()

if not document_lines:
    print('Empty lines')
    exit(1)

with open(name + '.html', 'w+', encoding='utf-8') as file:
    lines = []
    lines.append('<head>\n\t<title>%s</title>\n</head>'%name)
    lines.append('<p>\n\t<h1>%s</h1>\n</p>'%name)
    for line in document_lines:
        if not line:
            continue
        if line.startswith('*'):
            lines.append('<p>\n\t<h2>%s</h2>\n</p>'%line)  
        elif line.startswith('ㄴ'):
            lines.append('<p>\n\t<h3>%s</h3>\n</p>'%line)
        else:
            lines.append('<p>\n\t<strong>%s</strong>\n</p>'%line)

    if not lines:
        print('Empty lines')
        exit(1)
    text = '\n'.join(lines)
    file.write(text)

file.close()
exit(0)
