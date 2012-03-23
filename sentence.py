# -*- coding: utf-8 -*-
import codecs

default_delimiters = set(u"""#\n\r\t ,.:?!"()[]{}。，、；：？！“”「」『』《》〈〉【】〖〗〔〕«»─（）﹝﹞…﹏＿‧""")
default_sentence_minlen = 2
def splitFile2Sentence(file):
    """Split article into sentences by delimiters

    """
    try:
        text_file = codecs.open(file, 'rt', 'utf8')
    except IOError:
        print 'cannot open', file
        return

    text = text_file.read()
    delimiters = default_delimiters

    sentence = []
    linetxt = ''
    for c in text:
        if c in delimiters:
            linetxt = ''.join(sentence)
            if len(linetxt) > default_sentence_minlen:
                yield linetxt
            sentence = []
        else:
            sentence.append(c)
    linetxt = ''.join(sentence)
    if len(linetxt) > default_sentence_minlen:
        yield linetxt

