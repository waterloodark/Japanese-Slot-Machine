p_replay = 1.0/7.3
p_win = 0.1822
p_bonus_big = 1.0/200.0
p_bonus_regular = 0
slotin_lottery = 3
payout_win  = 8
slotin_bonus_big = 1
payout_bonus_big  = 15
n_bonus_big = 20
n_bonus_regular = 0
p_lose = 1 - p_replay - p_win - p_bonus_regular - p_bonus_big
pv_lot = [p_lose, p_replay, p_win]
pv_lot = pv_lot + [p_bonus_big] + [0]*(n_bonus_big-1)
print(pv_lot)
print(sum(pv_lot))
pv_bb = []
for i in range(4,23):
    pv_bb.append( [0]*i + [1] + [0]*(22-i) )
pv_bb.append( [1] + [0] * 22)
P = [pv_lot, pv_lot, pv_lot]
P.extend(pv_bb)

#payout_rb = payout_bonus_regular                                                                                                       
payout_bb = payout_bonus_big

states = {(0, 0, 0): 1}

import datetime as dt


timestamp_1 = dt.datetime.now()
print(timestamp_1)
for i in range(400):
    states_new = {}
    #print(list(states.keys()))                                                                                                         
    for state in list(states.keys()):
        i = state[0]
        p_vec = P[state[0]]
        p = states[state]
        if i is 0 or i is 2:
            slot_in = slotin_lottery
            states_n = [[0, state[1] + slot_in, state[2], p_vec[0]],
                        [1, state[1] + slot_in, state[2], p_vec[1]],
                        [0, state[1] + slot_in, state[2] + payout_win, p_vec[2]],
                        [3, state[1] + slot_in, state[2], p_vec[3]]]
        elif i is 1:
            slot_in = 0
            states_n = [[0, state[1], state[2], p_vec[0]],
                        [1, state[1], state[2], p_vec[1]],
            states_n = [[0, state[1], state[2], p_vec[0]],
                        [1, state[1], state[2], p_vec[1]],
                        [0, state[1], state[2] + payout_win, p_vec[2]],
                        [3, state[1], state[2], p_vec[3]]]
        elif i in range(3,22):
            slot_in = slotin_bonus_big
            pay_out = payout_bb
            states_n = [[i + 1, state[1] + slot_in, state[2] + payout_bonus_big, 1]]
        elif i is 22:
            slot_in = slotin_bonus_big
            pay_out = payout_bb
            states_n = [[0, state[1] + slot_in, state[2] + payout_bonus_big, 1]]
        else:
            print("ERROR!")
            print(i)
        for s in states_n:
            state_tmp = (s[0], s[1], s[2])
            pp = s[3]
            if state_tmp in states_new.keys():
                states_new[state_tmp] += p * pp
            else:
                states_new[state_tmp] = p * pp
    states = states_new
    #print(states)                                                                                                                      

timestamp_2 = dt.datetime.now()
print(timestamp_2)
print(timestamp_2 - timestamp_1)
print(len(states))

slotin_mean = sum([key[1]*states[key] for key in list(states.keys())])
payout_mean = sum([key[2]*states[key] for key in list(states.keys())])

print(slotin_mean)
print(payout_mean)
print(payout_mean / slotin_mean)


import csv
with open('states-100-1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows([[key[0], key[1], states[key]] for key in list(states.keys())])
