import FlipCoinModel as FCM
head_prob = 0.5
timeSteps = 20
cohortNumber = 1000

myCohort = FCM.cohort(id=2, cohort_number=cohortNumber, head_prob=head_prob)
myCohort.simulate(timeSteps)

print('Average expected reward(dollars):', myCohort.get_ave_exp_value())