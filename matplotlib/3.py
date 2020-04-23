import matplotlib.pyplot as plt
import numpy as np

x = np.arange(20)
y = np.exp(x)

fig = plt.figure()

# 1 x и y=x
ax = fig.add_subplot(221)
ax.plot(x, x)
ax.grid(True)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y = x', fontsize=14)

# 2 x и y=exp(x) 
ax = fig.add_subplot(222)
ax.plot(x, y)
ax.grid(True)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y = exp(x)', fontsize=14)

# 3 x и y=exp(x). OY с log шкалой
ax = fig.add_subplot(223)
ax.set_yscale('log')    # log здесь - натуральный логарифм!
# для работы с типом axis -> ax.set_yscale('log') 
ax.plot(x, y)
ax.grid(True)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y = exp(x)', fontsize=14)
ax.set_title(u'OY log шкала', loc='center')

# 4  x и y=x. OX с log шкалой
ax = fig.add_subplot(224)
ax.set_xscale('log')    # log здесь - натуральный логарифм!
ax.plot(x, x)
ax.grid(True)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y = x', fontsize=14)
ax.set_title(u'OX log шкала', loc='center')

# Автоматическое форматирование риснука
plt.tight_layout() 

#save('pic_10_4_1', fmt='png')
#save('pic_10_4_1', fmt='pdf')

plt.show()
