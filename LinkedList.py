# DFA to accept strings ending with 'ab'

def dfa_accepts_string(string):
    state = 0
    for char in string:
        if state == 0:
            state = 1 if char == 'a' else 0
        elif state == 1:
            state = 2 if char == 'b' else 1 if char == 'a' else 0
        elif state == 2:
            state = 1 if char == 'a' else 0
    return state == 2

# Test
print("Accepted" if dfa_accepts_string("aaab") else "Rejected")