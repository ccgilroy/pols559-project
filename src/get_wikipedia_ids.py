#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import pickle
import wikipedia

wikipedia.set_rate_limiting(rate_limit=True)

lgb_table_df = pd.read_csv('data/lgb_table.csv')

lgb_table_df['pageid'] = np.nan

# redoing data collection to get page ids
lgb_pages = []
errors = []
for i, row in lgb_table_df.iterrows():
    if np.isnan(row['pageid']):
        name = row['Title']
        try:
            page = wikipedia.page(name, auto_suggest=False)
            lgb_table_df.loc[i, 'pageid'] = page.pageid
            lgb_pages.append(page)
        except Exception as e:
            print({'name': name, 'error': e})
            errors.append({'name': name, 'error': e})

np.isnan(lgb_table_df.iloc[0]['pageid'])
lgb_table_df['Title'][0]

lgb_table_df.loc[lgb_table_df.pageid.isna(), :]

# one page has disappeared since the first time I collected the data...
# add the page id manually
lgb_table_df.loc[lgb_table_df.Title == 'Miranda Prather', 'pageid'] = np.nan

lgb_table_df.pageid.describe()

lgb_table_df.to_csv('data/lgb_table_ids.csv', index=False)

# redo page collection
lgb_pages_df = pd.DataFrame(index=list(range(0, len(lgb_pages))),
                            columns=['title', 'pageid', 'url', 'summary', 'content'])

for i, page in enumerate(lgb_pages):
    lgb_pages_df['title'][i] = page.title
    lgb_pages_df['pageid'][i] = page.pageid
    lgb_pages_df['url'][i] = page.url
    lgb_pages_df['summary'][i] = page.summary
    lgb_pages_df['content'][i] = page.content

with open('data/raw/pkl/lgb_pages_df_v2.pkl', 'wb') as f:
    pickle.dump(lgb_pages_df, f)

lgb_pages_df.to_csv('data/lgb_pages_v2.csv', index=False)
