def H93_generate_paths(S0, r, v, row, cho_matrix):
''' 
Simulation of Heston (1993) index process.

S: NumPy array
simulated index level paths
'''
S = np.zeros((M + 1, I), dtype=np.float)
S[0] = S0
bias = 0.0
sdt = math.sqrt(dt)
for t in xrange(1, M + 1, 1):
ran = np.dot(cho_matrix, rand[:, t])
if momatch:
bias = np.mean(np.sqrt(v[t]) * ran[row] * sdt)
if s_disc == 'Log':
S[t] = S[t - 1] * np.exp((r - 0.5 * v[t]) * dt +
np.sqrt(v[t]) * ran[row] * sdt - bias)
elif s_disc == 'Naive':
S[t] = S[t - 1] * (math.exp(r * dt) +
np.sqrt(v[t]) * ran[row] * sdt - bias)
else:
print "No valid Euler scheme."
exit(0)
return S