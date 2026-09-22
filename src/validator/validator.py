class Validator:

    def __init__(self, dfa):
        self.dfa = dfa
    
    def validate_code(self, code):
        
        current_state = self.dfa.start_state

        transitions = []

        for step, symbol in enumerate(code, start=1):
            if symbol not in self.dfa.alphabet:

                transitions.append({
                    "step": step,
                    "symbol": symbol,
                    "current_state": current_state,
                    "next_state": "INVALID SYMBOL"
                })

                return {
                    "accepted": False,
                    "final_state": "INVALID SYMBOL",
                    "transitions": transitions
                }

            next_state = self.dfa.transition(current_state, symbol)

            if next_state == None:
                next_state = "{q25}"

            transitions.appennd({
                "step": step,
                "symbol": symbol,
                "current_state": current_state,
                "next_state": next_state
            })

            current_state = next_state
        
        return({
            "accepted": self.dfa.is_accepting(current_state),
            "final_state": current_state,
            "transitions": transitions
        })