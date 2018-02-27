import numpy as np
import scr.FigureSupport as Fig

class Game:

    def __init__(self, id, repeat_time, head_prop):

        self.id = id
        self.reward = -250
        self.average_reward = 0
        self.plot_reward=[]
        self.repeat_time = repeat_time
        self.head_prop = head_prop
        self.random = np.random
        self.random.seed(id)
        self.loss = 0

    def simulate(self):
        toss_result=[]
        for i in range (0,20):
            if self.random.sample() < self.head_prop:
                toss_result.append('Head')
            else:
                toss_result.append('Tail')

        for j in range (2,20):
            if (toss_result[j] == 'Head') and (toss_result[j-1] == 'Tail') and (toss_result[j-2] == 'Tail'):
                self.reward += 100

        return self.reward

    def repeat(self):

        for k in range (0, self.repeat_time):
            L = Game(self.id, self.repeat_time, self.head_prop)
            m = L.simulate()
            self.average_reward += m
            self.plot_reward.append(m)
            self.id += 1

        self.average_reward = self.average_reward/self.repeat_time

        return self.average_reward

    def plot(self):
        
        for k in range (0, self.repeat_time):
            L = Game(self.id, self.repeat_time, self.head_prop)
            m = L.simulate()
            self.plot_reward.append(m)
            self.id += 1

        return self.plot_reward

    def prop(self):

        for k in range (0, self.repeat_time):
            L = Game(self.id, self.repeat_time, self.head_prop)
            m = L.simulate()
            if m <= 0:
                self.loss += 1
            self.id += 1

        self.loss = self.loss/self.repeat_time

        return self.loss


Q = Game(1, 1000, 0.5)
obs = Q.plot()
max_reward = max(obs)
min_reward = min(obs)

print('The expected reward:', Q.repeat())
print('The minimum reward: ', min_reward)
print('The maximum reward: ', max_reward)
print('The probability of losing money: ', Q.prop())

obs = Q.plot()

mygraph = Fig.graph_histogram(
    observations=obs,
    title='Histogram of Reward',
    x_label='Reward',
    y_label='Count',
    x_range=[-350, 350])

