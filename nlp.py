import nltk
from nltk.corpus import brown
from nltk.tag import UnigramTagger
# fd = nltk.FreqDist(brown.words(categories='news'))
# cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
# most_freq_words = list(fd.keys())[:100]
# likely_tags = dict((words,cfd[words].max()) for words in most_freq_words)
# tagger = UnigramTagger(model = likely_tags,backoff = nltk.DefaultTagger('NN'))
# brown_news_tagged = brown.tagged_words(categories='news')
# tagged_sents = brown.tagged_sents(categories='news')
# # print(tagger.evaluate(brown_news_tagged)


from nltk.corpus import brown
from nltk.probability import FreqDist

tagged_sent = brown.tagged_sents(categories = 'news')
tags = [tag for sent in tagged_sent for (words,tag) in sent]
fd = FreqDist(tags)
print(fd.most_common(10))

#unigram tagger
from nltk.tag import UnigramTagger
tagged_sents = brown.tagged_sents(categories = 'news')
sents = brown.sents(categories = 'news')
