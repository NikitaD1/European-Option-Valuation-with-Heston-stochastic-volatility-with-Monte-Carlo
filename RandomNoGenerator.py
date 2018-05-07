def random_number_generator(M, I):
''' Function to generate pseudo-random numbers.

Parameters
==========
M: int
time steps
I: int
number of simulation paths
Returns
=======
rand: NumPy array
random number array
'''
if antipath:
rand = np.random.standard_normal((2, M + 1, I / 2))
rand = np.concatenate((rand, -rand), 2)
else:
rand = np.random.standard_normal((2, M + 1, I))
if momatch:
rand = rand / np.std(rand)
rand = rand - np.mean(rand)
return rand