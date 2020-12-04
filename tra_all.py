# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.kl import KLSummarizer

from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import sumy

LANGUAGE = "english"
# LANGUAGE = "chinese"
# SENTENCES_COUNT = 10
SENTENCES_COUNT = 3
File_Name = "seeking_alpha_JFROG.txt"
# File_Name = "value investment.txt"

def machine_summary(summarizer):
    parser = PlaintextParser.from_file(File_Name, Tokenizer(LANGUAGE))
    file_name = File_Name + '_' + str(summarizer).split(".")[3].split(" ")[0]
    with open(file_name + '.txt', 'w') as fw:
        print('The summarization of ' + str(summarizer).split(".")[3].split(" ")[0] + ':')
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            print(sentence)
            fw.write(str(sentence))
        fw.close()


if __name__ == "__main__":
    print('The summarization of human:')
    with open('true_summary.txt', 'r') as fr:
        sentences = fr.read()
        print(sentences)
        fr.close()
    print()

    stemmer = Stemmer(LANGUAGE)
    algorithms = [LsaSummarizer,
                  LuhnSummarizer,
                  # EdmundsonSummarizer,
                  TextRankSummarizer,
                  LexRankSummarizer,
                  SumBasicSummarizer,
                  KLSummarizer]

    for alg in algorithms:
        summarizer = alg(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        machine_summary(summarizer)
        print()
