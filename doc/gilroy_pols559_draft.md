---
title: "An exploratory analysis of crowdsourced biographies of LGB public figures"
author: Connor Gilroy
date: 2018-03-05
output:
    pdf_document:
        latex_engine: xelatex
header-includes:
    - \usepackage{indentfirst}
mainfont: Gentium Basic
monofont: InconsolataGo
fontsize: 12pt
---

\setlength\parindent{0.5cm}
\setlength{\parskip}{0em}
\linespread{1.6}\selectfont
\def\UrlBreaks{\do\/\do-\do\.}

# Introduction

If you use Google to search for a public figure, their Wikipedia entry is one of the first things that comes up. Google's own summary for the individual, displayed in a sidebar, is drawn from Wikipedia. At least on the public sphere of the Internet, Wikipedia biographies are the canonical representations of individual life narratives, despite having been written by a crowd of anonymous editors.

Wikipedia entries are interesting because they are supposed to be drawn from public, verifiable sources, and it violates social norms for people to write or edit entries about themselves. This is why, for instance, a bot monitors when Wikipedia pages are edited from IP addresses associated with the US Congress (https://twitter.com/congressedits).

Nevertheless, there are well-known biases in Wikipedia content. For instance, the large majority of Wikipedia editors are men, and there are gendered biases in the ways women are covered (Wagner et al 2015). Other marginalized groups have a similar stake in how they are represented on Wikipedia.

LGBT people are particularly aware of the politics of visibility in the public sphere. A public figure coming out as LGBT is, in itself, often newsworthy. Public narratives matter, from high-profile media campaigns such as the It Gets Better Project (https://itgetsbetter.org/) to curated lists of historical figures that were ostensibly LGBT.

We should see a tension between the marginalization of a historically poorly documented social group and
a politically and socially driven desire for visibility play out on the pages of Wikipedia. One area it should surface is in the content of entries about LGBT people, and it is this content that I explore in this paper.

# Data

The data are 2883 unique articles drawn from a list of notable lesbian, gay, and bisexual individuals on Wikipedia.

What is notable is, of course, subjective. For instance, Adam Rippon's page was updated almost immediately to include information about his 2018 Oscars attire. (Adam Rippon is not, as it happens, included on the list of LGB people, despite being one of the two first openly gay US Winter Olympians.)

# Methods

My initial goal is to apply a range of approaches to characterizing the contents of this data set, moving from more straightforward techniques to more complex ones.

## Topic modeling

For the topic models, I preprocess the article contents using the default preprocessor from `gensim`, which removes punctuation, whitespace, and numbers, filters stopwords and short words, and stems the text. I convert the texts to a bag of words representation, and thence to a tf-idf matrix.

Thus far, latent semantic indexing has given me much clearer topics than latent dirichlet allocation. For instance, from an LSI model with only two topics, the first is about literature and the arts, while the second is about politics.

```
[(0,
  '0.130*"film" + 0.114*"album" + 0.105*"music" + 0.102*"award" + 0.101*"elect" +
  0.087*"theatr" + 0.081*"isbn" + 0.080*"plai" + 0.077*"book" + 0.076*"perform"'),
 (1,
  '-0.373*"elect" + -0.204*"democrat" + 0.168*"album" + -0.161*"district" +
  -0.144*"senat" + -0.131*"parliament" + -0.126*"vote" + 0.123*"music" +
  -0.121*"legisl" + -0.119*"repres"')]
```

Looking at the article metadata from the original list confirms that many of the people on it are notable as writer, musicians, actors, politicians, activists, and so on. I have not attempted to assess whether these labels correspond to the topics. With five topics, other themes appear, such as one about sports (`'0.388*"olymp" + 0.276*"championship" + 0.269*"team" + 0.204*"skate"`...).

By contrast, LDA topics seem less interpretable, even for small values of K. In particular, most of the words in the topic lists appear to be proper names. With two topics, the first corresponds to the `film`... topic from above---but the second is largely Finnish and Eastern European names. (It is possible that a different metric for associating words with topics would produce a more sensible result.) I might be able to address this issue by discarding rare words, or by using a term-document matrix with values other than tf-idf weighting.

## Supervised learning

I was able to merge 2740 articles with their metadata. Of these, 1775 are identified as being about gay men ("G"), 639 about lesbians ("L") and 326 about bisexual people ("B"). I used a simple classifier, a pipeline of tf-idf preprocessing with an SVM model from `scikit-learn`, to predict category membership from the contents of the articles. With a 75%/25% train-test split, the classifier predicts gay men very accurately, lesbians reasonably accurately, and bisexual people very poorly. This likely relates to the imbalance of the initial classes.

```
   precision    recall  f1-score   support

B       0.71      0.06      0.12        78
G       0.93      0.99      0.96       447
L       0.77      0.96      0.86       160

avg / total       0.87      0.88      0.84       685
```

I have yet to explore which features are associated with these classifications.

## Word embeddings

I have downloaded the pretrained GloVe vectors from Wikipedia 2014 data and have found code to integrate these text files with `gensim`, using `gensim.scripts.glove2word2vec`. I may need to move from word2vec to doc2vec, because I imagine clusters of documents to be more informative than clusters of words.

## Generative neural networks

`char-rnn`, a recurrent neural network, is the neural network type that I have seen used to generate new texts in the style of existing ones. There is a (Lua) Torch implementation, but I hope to find a PyTorch implementation instead.
