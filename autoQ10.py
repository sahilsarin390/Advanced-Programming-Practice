from automata.fa.nfa import NFA
# NFA which accepts strings that ends with '01'
nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1','q0'}, '1': {'q0'}},
        'q1': {'1': {'q2'}},
        'q2': {}
    },
    initial_state='q0',
    final_states={'q2'}
)
for i in range(1,4):
    num = input("Enter the string :")
    if(nfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
