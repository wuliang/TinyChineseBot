#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from cobe import brain
from wordseg import WordSeg
from sentence import splitFile2Sentence

def main():
    if len(sys.argv) != 2:
        print "Usage:", sys.argv[0], " filename "
        print
        return

    file = sys.argv[1]
    bot = brain.Brain("brain.db")
    seg = WordSeg()

    for text in splitFile2Sentence(file):
        terms = seg.splitTerms(text)
        request = ' '.join(terms)
        print("QOS: %s" % request.encode("utf-8"));
        # get the answer
        response = bot.reply(request).encode("utf-8")
        print("BOT: %s" % response);
        # learn something new
        bot.learn(request)


    print("BOT: %s" % u'再见地球！');


if __name__=='__main__':
    main()
