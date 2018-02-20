from enum import Enum
import numpy as np


class coinstate(Enum):
    """State of coin"""
    HEAD = 1
    TAIL = 0


class game:
    def __init__(self, id, head_prob):
        self._id = id
        self._head_prob = head_prob
        self._rnd = np.random
        self._rnd.seed(self._id)
        self._flipResult = coinstate.HEAD
        self._trails = []
        self._reward = -250

    def simulate(self, n_time_steps):

        t = 0  # simulation time

        while t < n_time_steps:
            if self._rnd.sample() < self._head_prob:
                self._flipResult = coinstate.HEAD
                self._trails.append(self._flipResult)

            else:
                self._flipResult = coinstate.TAIL
                self._trails.append(self._flipResult)

            t += 1

    def get_exp_value(self, n_time_steps):
        i = 2

        while i < n_time_steps:
            if self._trails[i] == coinstate.HEAD and self._trails[i-1] == coinstate.TAIL and self._trails[i-2] == coinstate.TAIL:
                self._reward += 100
            i += 1

        return self._reward


class cohort:
    def __init__(self, id, cohort_number, head_prob):
        self._cohorts = []
        self._expValue = []
        n = 1
        while n <= cohort_number:
            cohort = game(id * cohort_number + n, head_prob)
            self._cohorts.append(cohort)
            n += 1

    def simulate(self, n_time_steps):
        for cohort in self._cohorts:
            cohort.simulate(n_time_steps)
            value = cohort.get_exp_value(n_time_steps)
            if not (value is None):
                self._expValue.append(value)

        return self._expValue

    def get_ave_exp_value(self):
        return sum(self._expValue) / len(self._expValue)
