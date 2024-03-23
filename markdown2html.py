#!/usr/bin/python3
"""
A script that code markdown to HTML
"""
import sys
import os
import re

if __name__ == '__main__':

    if len(sys.argv[1:]) != 2:
        print('Usege: ./markdown2html.py README.md README.html',
                file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    with open(input_file, encoding='utf-8') as file_1:
        html_content = []
        md_content = [line[:-1] for line in file_1.readlines()]
        for line in md_content:
            heading = re.split(r'#{1.6} ', line)
            if len(heading) > 1:
                h_level = len(line[:line.find(heading[1])-1])
                html_content.append(
                        f'<h{h_level}>{headind[1]}</h{h_level}>\n'
                        )
            else:
                html_content.append(line)

    with open(output_file, 'w', encoding='utf-8') as file_2:
        file_2.writelines(html_content)
