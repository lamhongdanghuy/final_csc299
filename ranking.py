"""
Similar to matching.py, but search returns an ordered (ranked) results. In matching.py the results
from search are logically unordered (could be returned in any order). If we want to return 10 "best"
results from search in this file, you can just take the first 10 results. For search in matching.py
"best" has to be defined externally to introduce logical order to the returned results.
"""

import json
import typing
import re

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

def search(query: str, ti: typing.List[str], documents: typing.List[str]):
    counts = dict()
    for i, doc in enumerate(documents):
        counts[i] = final(query=query, title=ti[i], document=doc)
    print(counts)
    indexes = sorted(range(len(documents)), key=counts.get, reverse=True)
    print(indexes)
    an_doc = [documents[i] for i in indexes]
    an_ti = [ti[i] for i in indexes]
    for i in range(10):
        print(str(i+1) + ") Title: " + an_ti[i] )
        print("Document: " + an_doc[i])
        print("----------------------------")
        print()

def run_search():
    with open(r'F:\Depaul\Search Engine\main\test.json') as fp:
        data = json.load(fp)
    documents = [record['init_text'] for record in data]
    title = [record['title'] for record in data]
    query = input("Please enter a query:")
    while query:
        (search(query, title, documents))
        query = input("Please enter a query (!!! for quit):")
        if query == "!!!":
            break
