#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random

def make_game(game_name):
    if game_name == 'TicTacToe':
        return TicTacToegame()

class TicTacToegame():

    def __init__(self):
        self.reset_game()

    def render_board(self):
        line = '\n-----------\n'
        row = " {} | {} | {}"
        print((row + line + row + line + row).format(*self.state))
        print(self.info)

    def step_check(self, action):
        self.state[action] = self.cur_player
        self.action_space.remove(action)
        self.check_end()
        if self.is_end:
            if self.is_win:
                self.info = 'player{} win!'.format(self.cur_player)
            else:
                self.info = 'players draw'
        else:
            self.info = 'player{} turn'.format(self.cur_player)
        return (self.state, self.is_win, self.is_end, self.info)

    def reset_game(self, X=None, O=None):
        self.state = [' '] * 9
        self.action_space = list(range(9))
        self.is_end = False
        self.is_win = False
        self.info = 'new game'
        self.playerX = X
        self.playerO = O
        self.cur_player = random.choice(['O','X'])
        return (self.state, self.is_win, self.is_end, self.info)

    def player_turn(self):
        while 1:
            if self.cur_player == 'O':
                cur = self.playerO
                oth = self.playerX
            else:
                cur = self.playerX
                oth = self.playerO
            
            self.info = 'player{} turn'.format(self.cur_player) 
            yield (cur, oth)
            
            self.cur_player = 'OX'.replace(self.cur_player, '')

    def check_end(self):
        for a,b,c in [(0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]:
            if self.cur_player == self.state[a] == self.state[b] == self.state[c]:
                self.is_win = True
                self.is_end = True
                return

        if not any([s == ' ' for s in self.state]):
            self.is_win = False
            self.is_end = True
            return

class RandomPlayer():
    def __init__(self):
        self.name = 'Random'
        self.win_n = 0

    def action(self, state, actions):
        return random.choice(actions)

    def reward(self, reward, state):
        if reward == 1:
            self.win_n += 1

    def episode_end(self, episode):
        pass

class QLearningPlayer():
    def __init__(self):
        self.name = 'Q-Learning'
        self.q = {}
        self.init_q = 1 # "optimistic" 1.0 initial values
        self.lr = 0.3
        self.gamma = 0.9
        self.epsilon = 1.0
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01
        self.decay_rate = 0.01
        self.action_n = 9
        self.win_n = 0

        self.last_state = (' ',) * 9
        self.last_action = -1

    def action(self, state, actions):
        state = tuple(state)
        self.last_state = state

        r = random.uniform(0, 1)
        if r > self.epsilon:
            if self.q.get(state):
                i = np.argmax([self.q[state][a] for a in actions])
                action = actions[i]
            else:
                self.q[state] = [self.init_q] * self.action_n
                action = random.choice(actions)
        else:
            action = random.choice(actions)

        self.last_action = action
        return action

    def reward(self, reward, state):
        if self.last_action >= 0:
            if reward == 1:
                self.win_n += 1

            state = tuple(state)
            if self.q.get(self.last_state):
                q = self.q[self.last_state][self.last_action]
            else:
                self.q[self.last_state] = [self.init_q] * self.action_n
                q = self.init_q

            self.q[self.last_state][self.last_action] = q + self.lr * (reward + self.gamma * np.max(self.q.get(state, [self.init_q]*self.action_n)) - q)

    def episode_end(self, episode):
        # epsilon decay
        self.epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon) * np.exp(-self.decay_rate*(episode+1))

    def print_q(self):
        for k,v in self.q.items():
            print(k,v)

class HumanPlayer():
    def __init__(self):
        self.name = 'Human'

    def action(self, state, actions):
        a = int(input('your move:')) - 1
        return a


def train(trails_num, p1, p2, env):
    for episode in range(trails_num):
        
        state, win, done, info = env.reset_game(X=p1, O=p2)

        for (cur_player, oth_player) in env.player_turn():
            #env.render()
            action = cur_player.action(state, env.action_space)
            state, win, done, info = env.step_check(action)

            if done:
                if win:
                    cur_player.reward(1, state)
                    oth_player.reward(-1, state)
                else:
                    cur_player.reward(0.5, state)
                    oth_player.reward(0.5, state)
                break
            else:
                oth_player.reward(0, state)
        
        env.playerX.episode_end(episode)
        env.playerO.episode_end(episode)
    
    print('='*20)
    print('Train result - %d episodes' % trails_num)
    print('{} win rate: {}'.format(play_1.name, play_1.win_n / trails_num))
    print('{} win rate: {}'.format(play_2.name, play_2.win_n / trails_num))
    print('players draw rate: {}'.format((trails_num - play_1.win_n - play_2.win_n) / trails_num))
    print('='*20)


def play_game(play_1, play_2, env):
    while 1:
        state, win, done, info = env.reset_game(X=play_1, O=play_2)
        for (cp, op) in env.player_turn():
            print()
            env.render_board()
            action = cp.action(state, env.action_space)
            state, win, done, info = env.step_check(action)
            if done:
                env.render_board()
                break

if __name__ == '__main__':
    env = make_game('TicTacToe')
    play_1 = QLearningPlayer()
    play_2 = QLearningPlayer()
    play_3 = HumanPlayer()
    play_4 = RandomPlayer()
    train(10, play_1, play_4, env)
    play_game(play_1, play_3, env)


# In[ ]:




