p_free = 1/7.3
p_hand = 0.1634
p_rb = 1/315
p_bb = 1/259
p_blank = 1 - p_free - p_hand - p_rb - p_bb
payout_hand = 8
payout_rb = 8
payout_bb = 15
slotin_free = 0
slotin_lottary = 3
slotin_bonus_regular = 3
slotin_bonus_big = 3
state_lottary = [0, 2, 11, 26]
state_free = [1]
P = [[p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(len(P))
#for i in range(len(P)):                                                                                                                
#    print(len(P[i]))                                                                                                                   
s = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
states = {(0, 0): 1}

import datetime as dt

timestamp_1 = dt.datetime.now()
for i in range(6000):
    states_new = {}
    for state in list(states.keys()):
        p_vec = P[state[0]]
        for i in range(len(p_vec)):
            if p_vec[i] > 0:
                if i is 1:
                    slot_in = 0
                else:
                    slot_in = 3
                if i is 2:
                    pay_out = payout_hand
                elif i in range(3,10):
                    pay_out = payout_rb
                    state_next = (i + 1, state[1] - slot_in + pay_out)
                elif i is 10:
                    pay_out = payout_rb
                    state_next = (0, state[1] - slot_in + pay_out)
                elif i in range(11,25):
                    pay_out = payout_bb
                    state_next = (i + 1, state[1] - slot_in + pay_out)
                elif i is 25:
                    pay_out = payout_bb
                    state_next = (0, state[1] - slot_in + pay_out)
                else:
                    pay_out = 0
                    state_next = (0, state[1] - slot_in + pay_out)
                if state_next in states_new.keys():
                    states_new[state_next] += states[state] * p_vec[i]
                else:
                    states_new[state_next] = states[state] * p_vec[i]
    states = states_new
timestamp_2 = dt.datetime.now()
# print(states)                                                                                                                         
print(timestamp_1)
print(timestamp_2)
print(timestamp_2 - timestamp_1)
print(len(states))
