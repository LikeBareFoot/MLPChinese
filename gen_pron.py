#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pypinyin import pinyin, lazy_pinyin
import pypinyin

def inject_file(fw, file_name):
    with open(file_name, 'r') as fo:
        fw.write(fo.read())

def mark_pron(base_dir, file_name, withCh, withPron):
    output_filename = '{}/{}.html'.format(base_dir, file_name)
    
    print(file_name)
    print(output_filename)

    small = "small"
    big = "big"

    if withPron and withCh:
        pron_style = small
        ch_style = big
    
    if withPron and not withCh:
        pron_style = big 
        ch_style = big
    
    if not withPron and withCh:
        pron_style = small
        ch_style = big

    i = 0;
    with open(output_filename, 'w') as fw:
        fw.write("<html><head><meta charset=\"UTF-8\"><title>{}</title>".format(file_name));
        inject_file(fw, './cardstyle.css');
        inject_file(fw, './toggleVisibility.js');
        fw.write("</head><body>\n");
        fw.write("<button onclick=\"toggleDisplay(this, '{}')\" value='1'>隐藏拼音</button>".format(pron_style));
        fw.write("<table><tbody>");
        with open('{}/{}'.format(base_dir, file_name)) as fo:
            for line_of_text in fo:
                fw.write("<tr>\n")
                for ch in line_of_text.strip().split():
                    pron = pinyin(ch)
                    i = i + 1
                    fw.write("<td>\n")
                    if withPron:
                        fw.write("<div id=\"pron{}\" class=\"{}\">{}</div>".format(i, pron_style, pron[0][0]))
                    if withCh:
                        fw.write("<div class=\"{}\" onclick=\"toggleIdVisibility('pron{}')\">{}</div>".format(ch_style,i, ch))
                    fw.write("</td>\n")
                fw.write("</tr>\n")
        fw.write("</tbody></table>")
        fw.write("</body></html>\n")


if __name__ == '__main__':
    mark_pron('/workplace/Git/MLPCards', 'Grade1', True, True)
    mark_pron('/workplace/Git/MLPCards', 'Grade2', True, True)
    mark_pron('/workplace/Git/MLPCards', 'Grade3', True, True)
    mark_pron('/workplace/Git/MLPCards', 'Grade4', True, True)
    mark_pron('/workplace/Git/MLPCards', 'Grade5', True, True)


#https://www.heritagechinese.com/media/resources/5%E5%B9%B4%E7%BA%A7%E7%94%9F%E5%AD%97Poster.pdf
