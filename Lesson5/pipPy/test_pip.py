from isOdd import isOdd
from progress.bar import Bar
import time
import emoji
import matplotlib.pyplot as plt
import numpy as np

""" print(isOdd(0))
print(isOdd(4)) """


""" bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(1)
    # Do some work
    bar.next()
bar.finish() """



""" print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', language='alias'))
print(emoji.demojize('Python is 👍'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
print(emoji.is_emoji("👍")) """


""" # Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?') """

""" list = [1, 2, 3, 2 ,7]
plt.plot(list)

plt.show() """