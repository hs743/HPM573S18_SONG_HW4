import FlipCoinModel as FCM
head_prob = 0.5
timeSteps = 20
realizationNumber = 1000

myCohort = FCM.Realization(id=2, realization_number=realizationNumber, head_prob=head_prob)
myCohort.simulate(timeSteps)

print('Average expected reward(dollars):', myCohort.get_ave_exp_value())