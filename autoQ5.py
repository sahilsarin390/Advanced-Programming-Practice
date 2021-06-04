from automata.fa.dfa import DFA
# DFA which accepts repeated  ‘ab’ only.
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q3'},
        'q1': {'a': 'q3', 'b': 'q2'},
        'q2': {'a': 'q1', 'b': 'q3'},
        'q3': {'a': 'q3', 'b': 'q3'}
    },
    initial_state='q0',
    final_states={'q2'}
)
for i in range(1,6):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")