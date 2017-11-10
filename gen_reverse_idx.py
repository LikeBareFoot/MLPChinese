#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pypinyin import pinyin, lazy_pinyin
import pypinyin

def inject_file(fw, file_name):
    with open(file_name, 'r') as fo:
        fw.write(fo.read())


def gen_reverse_index(words_list_file):
    reverse_idx = dict()
    with open(words_list_file, 'r') as fo:
        for word in fo:
            word = word.strip()
            for ch in word:
                if ch in reverse_idx:
                    reverse_idx[ch].append(word)
                else:
                    reverse_idx[ch] = [word]
    return reverse_idx

def write_reverse_index(fw, base_dir, file_name, reverse_idx, col_count):
    i = 0
    with open('{}/{}'.format(base_dir, file_name)) as fo:
        for line_of_text in fo:
            for ch in line_of_text.strip().split():
                if ch in reverse_idx:
                    if i % col_count == 0:
                        fw.write("<tr>");
                    fw.write("<td><span class='ch'>{}</span></td>".format(ch))
                    fw.write("<td>")
                    for val in reverse_idx[ch]:
                        fw.write("<span class='word'>{}</span>".format(val))
                    fw.write("</td>")
                    if i % col_count == col_count - 1:
                        fw.write("</tr>\n");
                    i+=1

def make_word_list(base_dir, file_name, words_list_file, col_count,  withCh, withPron):
    output_filename = '{}/{}_words.html'.format(base_dir, file_name)
    r_idx = gen_reverse_index(words_list_file)
    
    print(file_name)
    print(output_filename)
#    print(r_idx)

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

    with open(output_filename, 'w') as fw:
        fw.write("<html><head><meta charset=\"UTF-8\"><title>{}</title>".format(file_name));
        inject_file(fw, './wordstyle.css');
        fw.write("</head><body>\n");
        fw.write("<table><tbody>")
        write_reverse_index(fw, base_dir, file_name, r_idx, col_count)
        fw.write("</tbody></table>")
        fw.write("</body></html>\n")


if __name__ == '__main__':
    make_word_list('/workplace/Git/MLPCards', 'Grade1', 'small.txt', 1, True, True)
    make_word_list('/workplace/Git/MLPCards', 'Grade2', 'small.txt', 1, True, True)
    make_word_list('/workplace/Git/MLPCards', 'Grade3', 'small.txt', 1, True, True)
    make_word_list('/workplace/Git/MLPCards', 'Grade4', 'small.txt', 1, True, True)
    make_word_list('/workplace/Git/MLPCards', 'Grade5', 'small.txt', 1, True, True)


#https://www.heritagechinese.com/media/resources/5%E5%B9%B4%E7%BA%A7%E7%94%9F%E5%AD%97Poster.pdf
