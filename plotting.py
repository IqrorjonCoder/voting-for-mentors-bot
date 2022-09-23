import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/Student/PycharmProjects/astrummentors/voting-mentors/mentors.db")
data = pd.read_sql("SELECT * FROM mentors WHERE mentors_name='Komiljon Xamidjonov'", conn)

print(data)