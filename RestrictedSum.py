#!/usr/bin/python
def checkio(data):
    return data[0] + checkio(data[1:]) if data else 0
