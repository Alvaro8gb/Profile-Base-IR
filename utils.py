import json 
import pickle
from models import List, Result, Query

def load_results(path:str):
    results = None
    with open(path) as f:
        results = json.load(f)
 
    return results

def dump_results(results, path):
    with open(path, 'w') as archivo:
        json.dump(results, archivo, indent=2)


def load_corpus(path):
    with open(path, 'rb') as file:
        corpus = pickle.load(file)
    return corpus

def dump_corpus(path, corpus):
    with open(path, 'wb') as file:
        pickle.dump(corpus, file)


def print_resuts(results:List[Result]):
     for i, r in enumerate(results):
            print(f" {i+1}. [ Score = {round(r.score,3):.3f} ] Category {r.category} |  ID: {r.id} | Text: {r.content[:50]}") 


def process_results(model, quereis:list[Query]):
    results_eval = []
    relevances = []

    for i, q in enumerate(quereis):
        print(f"Query {i+1}: {q}")
        results = model.launch_query(q.content) 
        print("-----")
        results_q = []
        relevances_q = []
        for j, r in enumerate(results): 
            results_q.append(r.id)
            relevances_q.append(1 if r.category == q.category else -1)

        results_eval.append(results_q)
        relevances.append(relevances_q)

    return results_eval, relevances