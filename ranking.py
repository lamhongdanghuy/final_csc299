"""
Similar to matching.py, but search returns an ordered (ranked) results. In matching.py the results
from search are logically unordered (could be returned in any order). If we want to return 10 "best"
results from search in this file, you can just take the first 10 results. For search in matching.py
"best" has to be defined externally to introduce logical order to the returned results.
"""

import json
import re
import typing


def final(query: str, title: str, document: str) -> int:
    point = 0
    query = re.sub(r'[^\w\s]', '', query)
    title = re.sub(r'[^\w\s]', '', title)
    document = re.sub(r'[^\w\s]', '', document)
    lower_query = query.lower()
    lower_title = title.lower()
    lower_document = document.lower()
    query_terms = [*set(lower_query.split())]
    title_terms = lower_title.split()
    document_terms = lower_document.split()

    if lower_query in lower_title:
        point += lower_title.count(lower_query) * len(lower_query.split()) * 4

        new_title = lower_title.replace(lower_query, "").lower().split()
        for word in query_terms:
            if word in new_title:
                point += new_title.count(word) * 3
    else:
        for word in query_terms:
            if word in title_terms:
                point += title_terms.count(word) * 3

    if lower_query in lower_document:
        point += lower_document.count(lower_query) * len(lower_query.split()) * 2
        new_doc = lower_document.replace(lower_query, "").split()
        for word in query_terms:
            if word in new_doc:
                point += new_doc.count(word)
    else:
        for word in query_terms:
            if word in document_terms:
                point += document_terms.count(word)

    return point


def term_count(query: str, document: str) -> int:
    count = 0
    query_terms = query.lower().split()
    document_terms = document.lower().split()
    for query_term in query_terms:
        for document_term in document_terms:
            if query_term == document_term:
                count += 1
    return count


def boolean_term_count(query: str, document: str) -> int:
    count = 0
    query_terms = query.lower().split()
    document_terms = document.lower().split()
    for term in query_terms:
        if term in document_terms:
            count += 1
    return count


def search(query: str, documents: typing.List[str]) -> typing.List[str]:
    counts = dict()
    for i, doc in enumerate(documents):
        counts[i] = term_count(query=query, document=doc)
    indexes = sorted(range(len(documents)), key=counts.get, reverse=True)
    return [documents[i] for i in indexes]


def run_search():
    with open(r'C:\Users\Alex\Documents\DePaul\datasets\wiki_small\wiki_small.json') as fp:
        data = json.load(fp)

    documents = [record['init_text'] for record in data]
    query = input("Please enter a query:")
    while query:
        print(search(query, documents))
        query = input("Please enter a query:")
