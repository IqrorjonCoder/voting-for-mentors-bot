import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/Student/PycharmProjects/astrummentors/voting-mentors/mentors.db")
data = pd.read_sql("SELECT * FROM mentors WHERE mentors_name='Komiljon Xamidjonov'", conn)

namunali = data.groupby('result').size().to_dict()['namunali']
namunali_ = pd.read_sql("SELECT * FROM mentors WHERE mentors_name='Komiljon Xamidjonov' and result='namunali'", conn).groupby('becauseof').size().to_dict()

qoniqarli = data.groupby('result').size().to_dict()['qoniqarli']
qoniqarli_ = data.groupby('result').size().to_dict()['qoniqarli']

qoniqarsiz = data.groupby('result').size().to_dict()['qoniqarsiz']
qoniqarsiz_= data.groupby('result').size().to_dict()['qoniqarsiz']

print(namunali_)

fig, axs = plt.subplots(2,2)
#
axs[0, 0].pie([namunali, qoniqarli, qoniqarsiz], labels=["namunali", "qoniqarli", "qoniqarsiz"], startangle=45)

axs[0, 1].pie([namunali_['barcha savolimga javob berdi'], namunali_['juda ham yaxshi tushuntirdi'], namunali_["o'z vaqtida ish joyida"], namunali_["yangicha va qiziqarli usulda taqdimot qilib tushuntirdi"]], colors=["b"], explode=(0.1,0.1,0.1, 0.1))
axs[0,1].legend()

axs[1,0].pie([namunali, qoniqarli, qoniqarsiz])

axs[1,1].pie([namunali, qoniqarli, qoniqarsiz])


plt.legend()
plt.show()