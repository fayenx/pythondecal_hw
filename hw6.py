# Question 1

import numpy as np
import matplotlib.pyplot as plt

def sinusoid(x, A, w):
    return A * np.sin(w * x)

x = np.linspace(0, 2 * np.pi, 1000)
A_values = np.linspace(1, 5, 5)  
w_values = np.linspace(0.5, 2.5, 5)

plt.figure(figsize=(10, 6))

for A, w in zip(A_values, w_values):
    y = sinusoid(x, A, w) 
    plt.plot(x, y, label=f'A={A}, w={w}') 

plt.xlabel('x')
plt.ylabel('y')
plt.title('Multiple Sinusoidal Waves')
plt.legend()

plt.show()


# Queation 2

import numpy as np
import matplotlib.pyplot as plt
list1 = np.random.randint(0, 101, 40)
list2 = np.random.randint(0, 101, 40)

plt.figure(figsize=(12, 6))

plt.plot(range(40), list1, color='orange', linewidth=10, label='Orange Line')
plt.plot(range(40), list2, color='red', linestyle='--', label='Red Dashed Line')

plt.xlabel('Index')
plt.ylabel('Random Value')
plt.title('Plot of Random Data')
plt.legend()

plt.show()
