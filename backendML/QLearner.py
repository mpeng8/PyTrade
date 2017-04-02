"""
Q-learner for RLStrateger 
"""

import numpy as np
import random as rand

class QLearner(object):

    def __init__(self, \
        num_states=100, \
        num_actions = 4, \
        alpha = 0.2, \
        gamma = 0.9, \
        rar = 0.5, \
        radr = 0.99, \
        dyna = 0, \
        verbose = False):

        self.verbose = verbose
        self.num_actions = num_actions
        self.s = 0
        self.a = 0
        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna
        self.Q = np.random.uniform(low = -1.0, high = 1.0, size=(num_states, num_actions))
        self.model = np.zeros((2,num_states,num_actions))
        self.prev = []
        

    def querysetstate(self, s):
        """
        @summary: Update the state without updating the Q-table
        @param s: The new state
        @returns: The selected action
        """
        self.s = s
        action = np.argmax(self.Q[s])
        self.a = action
        if self.verbose: print "s =", s,"a =",action
        return action

    def query(self,s_prime,r):
        """
        @summary: Update the Q table and return an action
        @param s_prime: The new state
        @param r: The ne state
        @returns: The selected action
        """
        action_prime = np.argmax(self.Q[s_prime])
        self.Q[self.s, self.a] = (1-self.alpha)*self.Q[self.s,self.a]+self.alpha*(r+self.Q[s_prime,action_prime])
        if (self.dyna != 0):
            self.model[0, self.s, self.a] = s_prime
            self.model[1, self.s, self.a] = r
            rand_arr = np.argwhere((self.model[1]!=0) & (self.model[1]!=-100))
            rand_list = np.random.randint(len(rand_arr), size=self.dyna)
            for i in range(0, self.dyna):
                rand_idx = rand_list[i]                
                rand_argidx = rand_arr[rand_idx]
                rand_s = rand_argidx[0]
                rand_a = rand_argidx[1]
                rand_s_prime = self.model[0,rand_s,rand_a]
                rand_r = self.model[1,rand_s,rand_a]
                rand_a_prime = np.argmax(self.Q[rand_s_prime])
                self.Q[rand_s, rand_a] = (1-self.alpha)*self.Q[rand_s,rand_a]+self.alpha*(rand_r+self.Q[rand_s_prime,rand_a_prime])
        if rand.uniform(0.0, 1.0) < self.rar:
            action = rand.randint(0, self.num_actions - 1)
        else:
            action = action_prime
        self.rar *= self.radr
        if self.verbose: print "s =", s_prime,"a =", action,"r =",r
        self.s = s_prime
        self.a = action
        return action
            
