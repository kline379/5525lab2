import hmms
import helpers

data = helpers.get_data()
initial_params = helpers.get_initial_params()

viterbi = hmms.viterbi(data, initial_params)
print "Viterbi:"
print viterbi

forward_backward = hmms.forward_backward(data, initial_params)
print "Forward-backward:"
print forward_backward
