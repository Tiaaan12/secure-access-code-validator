from automata.dfa import dfa
from validator.validator import Validator

validator = Validator(dfa)

code = input("Enter the code to validate: ")
result = validator.validate_code(code)

print('Accepted: ', result['accepted'])
print('Final State: ', result['final_state'])
for transition in result['transitions']:
    print(f"Step {transition['step']}: Symbol '{transition['symbol']}' - Current State: {transition['current_state']} -> Next State: {transition['next_state']}")