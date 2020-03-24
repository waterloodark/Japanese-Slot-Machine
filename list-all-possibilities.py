import datetime as dt
import matplotlib.pyplot as plt


class SlotMachine:
    def __init__(self):
        self.P = None

    def model_type_a(self, pr, r, slotin, payout):
        pr_lose, pr_win, pr_replay, pr_bb, pr_rb = pr
        r_bb, r_rb = r
        slotin_lottery, slotin_bb, slotin_rb = slotin
        payout_win, payout_bb, payout_rb = payout
        p_lottery = [pr_lose, pr_win, pr_replay]
        if r_bb > 0:
            p_lottery = p_lottery + [pr_bb] + [0] * (r_bb -1)
        if r_rb > 0:
            p_lottery = p_lottery + [pr_rb] + [0] * (r_rb -1)
        self.P = []
        self.P = [p_lottery, p_lottery, p_lottery]
        if r_bb > 0:
            p_bb = []
            for i in range(r_bb - 1):
                p_bb.append([0] * 3 + \
                            [0] * (i + 1) + [1] + [0] * (r_bb - i - 2) + \
                            [0] * r_rb)
            self.P = self.P + p_bb + [p_lottery]
        if r_rb > 0:
            p_rb = []
            for i in range(r_rb - 1):
                p_rb.append([0] * 3 + \
                            [0] * r_bb + \
                            [0] * (i + 1) + \
                            [1] + [0] * (r_rb - i - 2))
            self.P = self.P + p_rb + [p_lottery]

        # 状態数
        self.n_state = 1 + 1 + 1 + r_bb + r_rb

        # 払い出しメダル数
        self.payout = [0] * 3 + [payout_bb] * r_bb + [payout_rb] * r_rb

        # 投入メダル数
        self.slotin = [slotin_lottery] * 2 + [0] + \
                      [slotin_bb] * r_bb + [slotin_rb] * r_rb

    def configure(self, model):
        if model == 1:
            pr_replay = 1.0/7.3  # 再遊技発生確率
            pr_win = 0.1822  # 入賞確率
            pr_bb = 1.0/200.0  # BB当選確率
            pr_rb = 0.0  # RB当選確率

            slotin_lottery = 3  # メダル投入数 （抽選)
            payout_win = 8  # メダル払い出し数 (入賞)
            r_bb = 20  # BB繰り返し数
            slotin_bb = 1  # メダル投入数 (BB)
            payout_bb = 15  # メダル払い出し数 (BB)
            r_rb = 0  # RB繰り返し数
            slotin_rb = 1  # メダル投入数 (RB)
            payout_rb = 15  # メダル払い出し数 (RB)

        elif model == 2:
            pr_replay = 1.0/7.3  # 再遊技発生確率
            pr_win = 0.1614  # 入賞確率
            pr_bb = 1.0/250.0  # BB当選確率
            pr_rb = 1.0/250.0  # RB当選確率

            slotin_lottery = 3  # メダル投入数 （抽選)
            payout_win = 8  # メダル払い出し数 (入賞)
            r_bb = 20  # BB繰り返し数
            slotin_bb = 1  # メダル投入数 (BB)
            payout_bb = 15  # メダル払い出し数 (BB)
            r_rb = 8  # RB繰り返し数
            slotin_rb = 1  # メダル投入数 (RB)
            payout_rb = 15  # メダル払い出し数 (RB)

        elif model == 3:
            pr_replay = 1.0/7.3  # 再遊技発生確率
            pr_win = 0.1724  # 入賞確率
            pr_bb = 1.0/250.0  # BB当選確率
            pr_rb = 1.0/250.0  # RB当選確率
 
            slotin_lottery = 3  # メダル投入数 （抽選)
            payout_win = 8  # メダル払い出し数 (入賞)
            r_bb = 21  # BB繰り返し数
            slotin_bb = 2  # メダル投入数 (BB)
            payout_bb = 14  # メダル払い出し数 (BB)
            r_rb = 8  # RB繰り返し数
            slotin_rb = 2  # メダル投入数 (RB)
            payout_rb = 14  # メダル払い出し数 (RB)

        pr_lose = 1.0 - pr_replay - pr_win - pr_rb - pr_bb  # 外れ確率
        self.model_type_a([pr_lose, pr_win, pr_replay, pr_bb, pr_rb],
                          [r_bb, r_rb], 
                          [slotin_lottery, slotin_bb, slotin_rb],
                          [payout_win, payout_bb, payout_rb])

    def initialize(self):
        self.states = {(0, 0, 0): 1}
        self.epoch = [[dt.datetime.now(), len(self.states)]]

    def update(self):
        states_new = {}
        for s in list(self.states.keys()):
            p_trans = self.P[s[0]]
            pr = self.states[s]
            slot_in = self.slotin[s[0]]
            s_trans = []
            for k in range(len(p_trans)):
                if p_trans[k]>0:
                    s_new = (k, s[1] + slot_in, s[2] + self.payout[k])
                    pp = p_trans[k]
                    if s_new in states_new.keys():
                        states_new[s_new] += pr * pp
                    else:
                        states_new[s_new] = pr * pp
                
        self.states = states_new
        self.epoch.append([dt.datetime.now(), len(self.states)])
timestamp_begin = dt.datetime.now()
m = SlotMachine()
m.configure(1)
#for i in range(len(m.P)):
#    print(m.P[i])
#print([len(m.P), [len(m.P[i]) for i in range(len(m.P))]])
#print(m.slotin)
#print(m.payout)
m.initialize()
for i in range(1600):
    m.update()
print(len(m.states))
print(sum(m.states.values()))
timestamp_end = dt.datetime.now()
print(timestamp_end - timestamp_begin)

slotin_mean = sum([key[1]*m.states[key] for key in list(m.states.keys())])
payout_mean = sum([key[2]*m.states[key] for key in list(m.states.keys())])

print(slotin_mean)
print(payout_mean)
print(payout_mean / slotin_mean)

import csv
with open('states-1600-1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows([[key[1], key[2], m.states[key]] for key in list(m.states.keys())])
