#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import re
import wikipedia

from bs4 import BeautifulSoup

wikipedia.set_rate_limiting(rate_limit=True)

# 1. Get page 'List of gay, lesbian or bisexual people'
lgb_list_page = wikipedia.page('List of gay, lesbian or bisexual people')

# 2. Get links from page
lgb_links = lgb_list_page.links

# 3. Get subset of links using regex
p = re.compile('^List of gay, lesbian or bisexual people: *')
lgb_list_subpage_titles = list(filter(p.match, lgb_links))

# 4. For each link, get page
lgb_list_subpages = []
for title in lgb_list_subpage_titles:
    page = wikipedia.page(title, auto_suggest=False, redirect=False)
    lgb_list_subpages.append(page)

# 5. For each page, get html
lgb_list_subpages_html = []
for page in lgb_list_subpages:
    html = page.html()
    lgb_list_subpages_html.append(html)
    file_name = page.url.split('/')[-1].replace(':', '').replace(',', '')
    with open('data/raw/html/{}_{}.html'.format(file_name, page.pageid), 'wb') as f:
        f.write(html.encode('utf-8'))

# 6. For each html, get table
lgb_list_subpages_tables = []
for html in lgb_list_subpages_html:
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='wikitable sortable')
    lgb_list_subpages_tables.append(table)

# 7. Parse each table
def parse_lgb_table(table):
    table_list = []
    for row in table.find_all('tr')[1:-1]:
        try:
            cells = row.find_all('td')
            r_dict = {}
            name = cells[0].find('a')
            if name is not None:
                r_dict['Name'] = name.text
                r_dict['Title'] = name.attrs['title']
            else:
                # Ignore table rows that don't link to wiki pages
                continue
            lifetime = cells[1].find('span', class_='sorttext')
            if lifetime is not None:
                r_dict['Lifetime'] = lifetime.text
            else:
                r_dict['Lifetime'] = ', '.join(cells[1].stripped_strings)
            r_dict['Nationality'] = cells[2].text.strip()
            r_dict['Notable as'] = cells[3].text.strip()
            r_dict['Notes'] = list(cells[4].stripped_strings)[0]
            table_list.append(r_dict)
        except Exception as e:
            print({'error': e, 'row': row})
    return table_list

lgb_list_subpages_dicts = []
for table in lgb_list_subpages_tables:
    table_list = parse_lgb_table(table)
    lgb_list_subpages_dicts.append(table_list)

# 8. Convert to data frame
lgb_dicts_flattened = []
for l in lgb_list_subpages_dicts:
    lgb_dicts_flattened.extend(l)

col_names = ['Name', 'Title', 'Lifetime', 'Nationality', 'Notable as', 'Notes']
lgb_table_df = pd.DataFrame(lgb_dicts_flattened, columns=col_names)

# 9. Save data frame as csv
lgb_table_df.to_csv('data/lgb_table.csv', index=False)
