# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from collections import defaultdict
from janome.tokenizer import Tokenizer
import nltk
import math


class Extractor(object):
    def __init__(self):
        self.documents = defaultdict(lambda: 0)
        self.trimmer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+)')
        self.tokenizer = Tokenizer()
        self.count = 0
        self.term_frequency = defaultdict(lambda: 0)
        self.inverse_document_frequency = defaultdict(list)

    def add(self, document):
        trimmed_document = self._trim(document)
        if trimmed_document != '':
            self.documents[self.count] = trimmed_document
            self.count += 1

    def _trim(self, document):
        return ''.join(self.trimmer.tokenize(document))

    def extract(self):
        for page, document in self.documents.iteritems():
            for token in self.tokenizer.tokenize(document):
                if '名詞' not in token.part_of_speech and '動詞' not in token.part_of_speech:
                    continue

                if '助動詞' in token.part_of_speech or '非自立' in token.part_of_speech or '接尾' in token.part_of_speech or '数' in token.part_of_speech:
                    continue

                if 'する' in token.base_form or 'やる' in token.base_form or 'なる' in token.base_form or 'ござる' in token.base_form:
                    continue

                self.term_frequency[token.base_form] += 1

                if page not in self.inverse_document_frequency[token.base_form]:
                    self.inverse_document_frequency[token.base_form].append(page)

        result = defaultdict(int)

        for term, frequency in self.term_frequency.iteritems():
            result[term] = frequency * math.log10(self.count/len(self.inverse_document_frequency[term]))

        return result
