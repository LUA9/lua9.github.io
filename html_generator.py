# -*- coding: utf-8 -*-
# mypy: ignore-errors

# 코드 정리를 안 해서 코드가 엉망입니다.
# 더욱 빠른 코드를 위해서는 pypy를 이용해주시기 바랍니다.

from argparse import ArgumentParser
from contextlib import closing

def clean(string):
    return string.rstrip().lstrip()

parser = ArgumentParser(usage='python -m html_generator <이름> <파일 위치>')
parser.add_argument('name')
parser.add_argument('location')

arguments = parser.parse_args()

with closing(open(arguments.location, 'r', encoding='UTF-8')) as document_file:
    content = document_file.read()

lines = content.splitlines()

if not lines:
    raise ValueError('파일이 비었습니다.')

with closing(open(arguments.name + '.html', 'w', encoding='UTF-8')) as file:
    result_lines = []
    result_lines.append(f'<head>\n\t<title>{arguments.name}</title>\n</head>')
    result_lines.append(f'<p>\n\t<h1>{arguments.name}</h1>\n</p>')

    for index, line in enumerate(lines, 1):
        line = clean(line)
        if not line:
            continue

        print(f'{index}번째 줄 작성 중...')

        if line.startswith('*'):
            result_lines.append(f'<p>\n\t<h2>{line}</h2>\n</p>')

        elif line.startswith('ㄴ'):
            result_lines.append(f'<p>\n\t<h3>{line}</h3>\n</p>')

        elif line.startswith('자료:'):
            result_lines.append(f'<p>\n\t<div>{line}</div>\n</p>')

        else:
            result_lines.append(f'<p>\n\t<strong>{line}</strong>\n</p>')

    if not lines:
        raise ValueError('알 수 없는 오류가 발생 했습니다.')

    text = '\n'.join(result_lines)
    file.write(text)

exit(0)
