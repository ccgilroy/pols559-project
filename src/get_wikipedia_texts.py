#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pickle
import wikipedia

wikipedia.set_rate_limiting(rate_limit=True)

lgb_table_df = pd.read_csv('data/lgb_table.csv')

lgb_pages = []
errors = []
for name in lgb_table_df['Title']:
    try:
        page = wikipedia.page(name, auto_suggest=False)
        lgb_pages.append(page)
        with open('data/txt/{}.txt'.format(page.pageid), 'wb') as f:
            f.write(page.content.encode('utf-8'))
    except Exception as e:
        print({'name': name, 'error': e})
        errors.append({'name': name, 'error': e})

with open('data/raw/pkl/lgb_pages.pkl', 'wb') as f:
    pickle.dump(lgb_pages, f)

with open('data/raw/pkl/errors.pkl', 'wb') as f:
    pickle.dump(errors, f)

# summary information
# lgb_table_df.shape
# len(lgb_pages)
# len(lgb_table_df['Title'].unique()) # 2890
# len(set(map(lambda x: x.title, lgb_pages)))

lgb_pages_df = pd.DataFrame(index=list(range(0, len(lgb_pages))),
                            columns=['title', 'pageid', 'url', 'summary', 'content'])

for i, page in enumerate(lgb_pages):
    lgb_pages_df['title'][i] = page.title
    lgb_pages_df['pageid'][i] = page.pageid
    lgb_pages_df['url'][i] = page.url
    lgb_pages_df['summary'][i] = page.summary
    lgb_pages_df['content'][i] = page.content

with open('data/raw/pkl/lgb_pages_df.pkl', 'wb') as f:
    pickle.dump(lgb_pages_df, f)

lgb_pages_df.to_csv('data/lgb_pages.csv', index=False)
