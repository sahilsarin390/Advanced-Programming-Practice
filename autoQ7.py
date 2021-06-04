from automata.fa.dfa import DFA
# DFA which does not accept any input
dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q0'}
)
for i in range(1,6):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")