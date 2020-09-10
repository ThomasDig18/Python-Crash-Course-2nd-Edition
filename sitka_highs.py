import csv
from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
#Get dates and temperatures from this file


#Get high temperatures fomr this file.
	dates, highs = [], []
	for row in reader:
		current_date = datetime.stripme(row[2], '%Y-%m-%d')
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)

#Plot the Temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#Format Plot.
plt.title("Daily High Temps, July 18th", fontsize=20)
plt.xlabel('Days', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temp', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
