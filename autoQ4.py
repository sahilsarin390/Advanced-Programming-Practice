from automata.fa.dfa import DFA
# DFA which accepts single 'a' or (aa)* ending with 'b'
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q5'},
        'q1': {'a': 'q2', 'b': 'q5'},
        'q2': {'a': 'q3', 'b': 'q4'},
        'q3': {'a': 'q2', 'b': 'q5'},
        'q4': {'a': 'q5', 'b': 'q5'},
        'q5': {'a': 'q5', 'b': 'q5'}
    },
    initial_state='q0',
    final_states={'q1', 'q4'}
)
for i in range(1,6):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
