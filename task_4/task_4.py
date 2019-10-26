import numpy as np
import matplotlib.pyplot as plt

X = np.random.sample((5, 5))

# Pareto front
pf = np.empty([0, X.shape[1]])
# not Pareto front
n_pf = np.empty([0, X.shape[1]])

# auxiliary array
b = np.empty([X.shape[1], 1])
b.fill(True)

for i in range(X.shape[0]):
    # compate X[i] with other vectors
    A = X[i]<=X
    
    # result is array, where number in i-place is a
    # number of True in A[i]
    res = A.dot(b)
    
    # condition means if there are more, then one vector (with the current vector)
    # which greater in every component, then current
    # it means, that current vector is not Pareto optimal
    if (np.sum(res==X.shape[1])>1):
        n_pf = np.vstack((n_pf, X[i]))
    else:
        pf = np.vstack((pf, X[i]))
        
fig = plt.figure(figsize=[10, 10])

# setting up view of diagrams
axs1 = fig.add_subplot(211)
axs1.set_xticks(np.arange(0, X.shape[1], 1))
axs2 = fig.add_subplot(212, projection="polar")
axs2.yaxis.grid(False)
axs2.set_yticks([])
plt.thetagrids(np.arange(0, 360, 360.0/X.shape[1]), labels=np.arange(0, X.shape[1], 1))
for i in range(X.shape[1]):
    axs1.axvline(x=i, linestyle="--", color="black", alpha=0.5)

axs1.set_title('Line')
axs2.set_title('Polar')

xPolar = np.arange(0, X.shape[1], 1)
xPolar = np.append(xPolar, 0)
xPolar = xPolar * 2 * 3.14 / X.shape[1]

for x in n_pf:    
    yPolar = np.append(x, x[0])
    axs1.plot(range(X.shape[1]), x, color="blue", alpha=0.3)
    axs2.plot(xPolar, yPolar, color="green")
    
for x in pf:
    yPolar = np.append(x, x[0])
    
    axs1.plot(range(X.shape[1]), x, color="red")
    axs2.plot(xPolar, yPolar, color="red")
