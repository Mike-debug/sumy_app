# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "chinese"
# SENTENCES_COUNT = 10

if __name__ == "__main__":
    # for html

    # url = "https://en.wikipedia.org/wiki/Automatic_summarization"
    url = "https://xueqiu.com/1156952266/164653613"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

    # or for plain text files

    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    # parser = PlaintextParser.from_file("seeking_alpha_JFROG.txt", Tokenizer(LANGUAGE))

    # or for string

    # parser = PlaintextParser.from_string("Check this out.", Tokenizer(LANGUAGE))

    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    with open('machine_summary.txt', 'w') as fw:
        print('The summarization of machine:')
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            print(sentence)
            fw.write(str(sentence))
        fw.close()
    print('\n\n\n')
    print('The summarization of human:')
    with open('true_summary.txt', 'r') as fr:
        sentences = fr.read()
        print(sentences)
        fr.close()
