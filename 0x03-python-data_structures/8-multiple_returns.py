#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return reversed(("None", 0))
    else:
        s_len = len(sentence)
        return (s_len, sentence[0])
