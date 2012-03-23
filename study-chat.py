#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import logging
from cobe import brain
from wordseg import WordSeg

def main():
    #logging.basicConfig(level=logging.DEBUG)
    bot = brain.Brain("brain.db")
    seg = WordSeg()

    quits = [u'再见', u'拜拜', u'quit', u'byebye']
    # it need word segmentation
    text = u"我说中文。"

    while True:
        if text in quits:
            break;
        terms = seg.splitTerms(text)
        request = ' '.join(terms)
        # get the answer
        response = bot.reply(request).encode("utf-8")
        print("BOT: %s" % response);
        # learn something new
        bot.learn(request)
        # next run let's input
        text = raw_input('QOS:').decode(sys.stdin.encoding)

    print("BOT: %s" % u'再见地球！');


if __name__=='__main__':
    main()

