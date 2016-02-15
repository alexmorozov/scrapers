#!/usr/bin/env python
#--coding: utf8--

"""
Print the highlighted words from the ESL podcast transcript.
"""

import argparse

from utils import Page


def scrape_words(url):
    page = Page(url)
    words = page.css('.podcast_table_home .pod_body b')
    return [word.text_content().lower().strip()
            for word in words]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    print u'\n'.join(scrape_words(args.url))
