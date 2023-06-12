#!/usr/bin/python3
def multiple_returns(sentence):
    tuples = 0, None
    if sentence != '':
        tuples = len(sentence), sentence[0]
    return tuples
