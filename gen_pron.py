#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pypinyin import pinyin, lazy_pinyin
import pypinyin
from gen_reverse_idx import gen_reverse_index

def inject_file(fw, file_name):
    with open(file_name, 'r') as fo:
        fw.write(fo.read())

def mark_pron(base_dir, file_name, word_list):
    output_filename = '{}/{}.html'.format(base_dir, file_name)
    reverse_idx = gen_reverse_index(word_list)
    
    print(file_name)
    print(output_filename)

    small = "small"
    big = "big"

    pron_style = small
    ch_style = big

    i = 0
    with open(output_filename, 'w') as fw:
        fw.write("<html><head><meta charset=\"UTF-8\"><title>{}</title>".format(file_name))
        inject_file(fw, './cardstyle.css')
        inject_file(fw, './toggleVisibility.js')
        fw.write("</head><body>\n")
        fw.write("<button onclick=\"toggleDisplay(this, '{}')\" value='1'>隐藏拼音</button>".format(pron_style))
        fw.write("<table><tbody>")
        with open('{}/{}'.format(base_dir, file_name)) as fo:
            for line_of_text in fo:
                fw.write("<tr>\n")
                for ch in line_of_text.strip().split():
                    pron = pinyin(ch)
                    i = i + 1
                    fw.write("<td>\n")
                    fw.write("<div id=\"pron{}\" class=\"{}\">{}</div>".format(i, pron_style, pron[0][0]))
                    fw.write("<div class=\"{}\" onclick=\"toggleIdVisibility('pron{}')\">{}".format(ch_style,i, ch))
                    write_words(fw, reverse_idx, ch)
                    fw.write("</div>")
                    fw.write("</td>\n")
                fw.write("</tr>\n")
        fw.write("</tbody></table>")
        fw.write("</body></html>\n")

def write_words(fw, reverse_idx, ch):
    if ch in reverse_idx:
        fw.write("<table class=\"tooltiptext\"><tr><td>")
        for val in reverse_idx[ch]:
            fw.write("<span class='word'>{}</span>".format(val))
        fw.write("</td></tr></table>")

if __name__ == '__main__':
    mark_pron('/workplace/MLPChinese', 'Grade1', 'PrimarySchoolWords')
    mark_pron('/workplace/MLPChinese', 'Grade2', 'PrimarySchoolWords')
    mark_pron('/workplace/MLPChinese', 'Grade3', 'PrimarySchoolWords')
    mark_pron('/workplace/MLPChinese', 'Grade4', 'PrimarySchoolWords')
    mark_pron('/workplace/MLPChinese', 'Grade5', 'PrimarySchoolWords')


#https://www.heritagechinese.com/media/resources/5%E5%B9%B4%E7%BA%A7%E7%94%9F%E5%AD%97Poster.pdf
