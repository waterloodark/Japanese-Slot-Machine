P = [[5/6, 1/6, 0],
     [0,   0,   1],
     [5/6, 1/6, 0]]
for k in range(3):
    print("{0:.3f}, {1:.3f}, {2:.3f}".format(P[k][0], P[k][1], P[k][2]))

s = [1, 0, 0]
reward = [0, 0, 5]
pay = [-1, -1, -1]

print(s)
print("{0:3d}: {1:.3f}, {2:.3f}, {3:.3f}".format(0, s[0], s[1], s[2]))

for ep in range(1, 10 + 1):
    s = [sum([s[i] * P[i][k] for i in range(3)]) for k in range(3)]
    print("{0:3d}: {1:.3f}, {2:.3f}, {3:.3f}".format(ep, s[0], s[1], s[2]))

s = [1, 0, 0]
P = [[5/6, 1/6, 0],
     [0,   0,   1],
     [5/6, 1/6, 0]]
states = {(0, 0): 1}
for i in range(10000):
    states_new = {}
    for state in list(states.keys()):
        p_vec = P[state[0]]
        for i in range(len(p_vec)):
            if p_vec[i]>0:
                if i<2:
                    if (i, state[1] - 1) in states_new.keys():
                        states_new[(i, state[1] - 1)] += states[state]*p_vec[i]
                    else:
                        states_new[(i, state[1] - 1)] = states[state]*p_vec[i]
                else:
                    if (i, state[1] + 5) in states_new.keys():
                        states_new[(i, state[1] + 5)] += states[state]
                    else:
                        states_new[(i, state[1] + 5)] = states[state]
    states = states_new
print(states)
