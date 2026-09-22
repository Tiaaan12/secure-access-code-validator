import json
from pathlib import Path

from .alphabet import (ALPHABET, START_STATE, ACCEPTING_STATES)

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def transition(self, state, symbol):
        if state not in self.states:
            raise ValueError(f"State {state} is not a valid state.")
        if symbol not in self.alphabet:
            raise ValueError(f"Symbol {symbol} is not in the alphabet.")
        return self.transition_function.get(state, {}).get(symbol, None)    

    def is_accepting(self, state):
        return state in self.accept_states

def load_dfa():

    base_dir = Path(__file__).resolve().parents[2]

    json_path = base_dir / "data" / "dfa.json"

    with open(json_path, "r", encoding="utf-8") as file:
        transition_function = json.load(file)

    states = set(transition_function.keys())

    return DFA(
        states=states,
        alphabet=ALPHABET,
        transition_function=transition_function,
        start_state=START_STATE,
        accept_states=ACCEPTING_STATES
    )

dfa = load_dfa()