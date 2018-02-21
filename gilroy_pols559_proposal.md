---
title: POLS 559 Topic Proposal
subtitle: Patterns and variations in LGBT Biographical Narratives
author: Connor Gilroy
date: 2018-02-14
output:
    pdf_document:
        latex_engine: xelatex
mainfont: Gentium Basic
fontsize: 12pt
---

# Research question

What are the key elements of LGBT life narratives? I propose to use feature extraction and text analysis to explore this question. I approach this project from a prior interest in coming-out narratives---how typical they are and what impacts they have on general perceptions of LGBT people---but want to take a broader, more life-course oriented view.

Both within and outside of sociology, the study of sexuality tends to illuminate the proliferation of identity categories, and deviations from norms. Because of this, my project needs to emphasize *variations* as well as trends.

# Data

I propose to use crowdsourced biographies from Wikipedia's [Lists of LGBT people](https://en.wikipedia.org/wiki/Lists_of_LGBT_people). specifically the [List of gay, lesbian or bisexual people](https://en.wikipedia.org/wiki/List_of_gay,_lesbian_or_bisexual_people) and the [List of transgender people](https://en.wikipedia.org/wiki/List_of_transgender_people). This kind of list is useful because it represents one sort of answer to the questions of which queer narratives circulate, which are visible in the public sphere, and which are considered "notable."

This data source will give me a corpus of several hundred articles. The table for the LGB list includes limited metadata as well: lifetime, nationality, reason for notability, and classification as lesbian, gay, or bisexual.

Part of my motivation is that I wanted to work with longer and more complex documents than e.g. tweets. I considered using transcripts of oral histories instead (http://lgbtqdigitalcollaboratory.org/oral-history-hub/), but existing collections seem to be restricted to narrow subjects, e.g. the HIV/AIDS-related activism of ACT UP.

One reasonable approach would be to compare these biographies to Wikipedia entries for heterosexual individuals, but I don't think that's the most interesting project. (Are queer narratives different from straight ones? You'd expect so. So what?) Machine-learning projects in other domains (e.g. Wang and Kosinski 2017 with facial recognition) have struggled to tackle that question in a theoretically-informed and ethical way. Data-wise, there also isn't a comparable list of non-LGBT people to sample from.

# Methods

Because what I propose is deliberately open-ended, I can bring to bear a range of methods:

- exploratory topic modeling to uncover *commonalities* across biographies
- supervised learning, to see what text features predict specific identity categories, and investigate *distinctions* between lesbian, gay, bisexual, and trans narratives
- word2vec to map or plot word meanings, using the pre-trained wikipedia GloVe vectors. This would be inspired by [Garg et al 2017](http://arxiv.org/abs/1711.08412) and [profCloud](http://benschmidt.org/profCloud/)
- generative neural networks, to uncover important features of narratives by generating new ones (as in Tiffany Chan's digital humanities [project](https://eltiffster.github.io/authorFunction/)).

# Outcomes

This project has several potential applications, including the ability to identify misclassified narratives---articles that *should* be on the list of LGBT people, but aren't. It will also identify features for me to look for in other sources, such as interview transcripts, or to ask about in survey questions. Finally, it will allow me to develop a technical framework for future research (particularly in terms of setting up the infrastructure to train neural networks).
