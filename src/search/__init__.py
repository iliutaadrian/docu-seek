from .fulltext_search import init as init_fulltext, search as search_fulltext
from .tfidf_search import init as init_tfidf, search as search_tfidf
from .bm25_search import init as init_bm25, search as search_bm25
from .openai_search import init as init_openai, search as search_openai
from .bert_search import init as init_bert, search as search_bert
from .sentence_transformers_search import init as init_sentence_transformers, search as search_sentence_transformers
from .hybrid_search import search as hybrid_search

def init_search_module(documents):
    init_fulltext(documents)
    init_tfidf(documents)
    init_bm25(documents)
    init_openai(documents)
    init_bert(documents)
    init_sentence_transformers(documents)
