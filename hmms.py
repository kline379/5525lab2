'''
function VITERBI(observations of len T, state-graph of len N) returns best-path
    create a path probability matrix viterbi[N+2,T]
    for each state s from 1 to N do
        viterbi[s,1]<-a_{0,s * b_s(o_1)
        backpointer[s,1]<-0
    for each time step t from 2 to T do
        for each state s from 1 to N do
            viterbi[s,t]<-max_{s'=1}^N viterbi[s', t-1] * a_{s',s} * b_s(o_t)
            backpointer[s,t]<-argmax_{s'=1}^N viterbi[s', t-1] * a_{s',s}
    viterbi[q_F, T]<-max_{s=1}^N viterbi[s,T] * a_{s,q_F}
    backpointer[q_F ,T]<-argmax_{s=1}^N viterbi[s,T] * a_{s,q_F}
    return the backtrace path by following backpointers to states back in
           time from backpointer[qF ,T]
'''
def viterbi(data, params):
    raise Exception('viterbi not implemented.')

'''
Runs the foward algorithm given the data and paramaters. Pseduocode below:
function FOWARD(observations of len T, state-graph of len N) returns forward-prob:
    create a probability matrix forward[N+2,T]
    for each state s from 1 to N do:
        forward[s,1]<-a_{0,s}*b_s(o_1)
    for each time step t from 1 to N do:
        forward[s,t]<- Sum_{s'=1}^N forward[s',t-1]*a_s*b_s(o_t)
    forward[q_F,T]<- Sum_{s=1}^N forward[s,T]*a{s,q_F}
    return forward[q_F, T]
'''
def forward(data, params):
    raise Exception('forward not implemented.')


'''
Runs the backward algorithm with the given paramaters. Psedocode below:
function BACKWARD(observations of len T, state-graph of len N) returns backward-prob:
    create a probability matrix backward[N+2,T]
    for each state s from 1 to N do:
        backward[s,T]<-b_{T,s}*b_s(o_T)
    for each time step t from N to 1 do:
        backward[s,t]<- Sum_{s'=1}^N backward[s',t-1]*a_s*b_s(o_t)
    backward[q_F,T]<- Sum_{s=1}^N forward[s,T]*a{s,q_F}
    return backward[q_F, T]
'''
def backward(data, params):
    raise Exception('backward not implemented.')

'''
Computes the new params for the forward-backward algorithm
'''
def computer_new_params(alpha, beta):
    raise Exception('backward not implemented.')

'''
Runs the forward-backward algorithm.
'''
def forward_backward(data, params, epsilon = .01):
    old_params = params + epsilon
    while(abs(params-old_params)<epsilon):
        alpha = forward(data, params)
        beta = backward(data, params)
        old_params = params
        params = compute_new_params(alpha, beta)
