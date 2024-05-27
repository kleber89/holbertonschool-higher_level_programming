#!/usr/bin/python3
def multiple_returns(frase):
    if len(frase) == 0:
        return (0, None)
    else:
        return (len(frase), frase[0])
