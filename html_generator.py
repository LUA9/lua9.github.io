# -*- coding: utf-8 -*-
# mypy: ignore-errors

from time import time
from argparse import ArgumentParser

start = time()

parser = ArgumentParser(usage='python -m 생성기 <>문서 <>문서 이름')
parser.add_argument('document')
parser.add_argument('name')

arguments = parser.parse_args()
document = arguments.document
name = arguments.name

with open(document, 'r+', encoding='UTF-8') as file:
    content = file.read()

lines = content.splitlines()

if not lines:
    raise ValueError('Empty file')

with open(name + '.html', 'w+', encoding='UTF-8') as file:
    result_lines = list()
    result_lines.append('<head>\n\t<title>%s</title>\n</head>'%name)
    result_lines.append('<p>\n\t<h1>%s</h1>\n</p>'%name)

    for index, line in enumerate(lines, 1):
        line = line.lstrip().rstrip()
        if not line:
            print('Empty: Line %d'%index)
            continue

        if '[]END' in line:
            print('END: Line %d'%index)
            break

        if line.startswith('*'):
            print('Write: Line %d'%index)
            result_lines.append('<p>\n\t<h2>%s</h2>\n</p>'%line)

        elif line.startswith('ㄴ'):
            print('Write: Line %d'%index)
            result_lines.append('<p>\n\t<h3>%s</h3>\n</p>'%line)

        elif line.startswith('자료:'):
            result_lines.append('<p>\n\t<div>%s</div>\n</p>'%line)

        else:
            print('Write: Line %d'%index)
            result_lines.append('<p>\n\t<strong>%s</strong>\n</p>'%line)

    if not lines:
        raise ValueError('Empty lines')

    text = '\n'.join(result_lines)
    file.write(text)

file.close()

end = time()
print('Done: {} seconds'.format(end - start))
exit(0)
