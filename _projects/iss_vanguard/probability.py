import json

# Basic dice: 4 basic, 1 vanguard, 1 bang
# Icon dice: 3 icon, 1 basic, 1 vanguard, 1 bang
# Vanguard dice: 2 vanguard, 1 double-vanguard, 3 bang

def calculate_probability(inputs):
    return {
            'inputs': inputs,
            'failure_probability': .1,
            'success_probability': .25,
    }
