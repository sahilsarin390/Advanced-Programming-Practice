from automata.fa.dfa import DFA
# DFA which does not accept any input
dfa = DFA(
    states={'q0'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q0'}
    },
    initial_state='q0',
    final_states={'q0'}
)
for i in range(1,8):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
