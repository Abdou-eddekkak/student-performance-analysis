import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#1. load the dataset
df = pd.read_csv('cleaned_student_data.csv')

plt.style.use('seaborn-v0_8-whitegrid')

# Chart 1: The Absence Penalty (Scatter Plot with Trendline)
plt.figure(figsize=(10, 6))
plt.scatter(df['absences'], df['G3'], alpha=0.5, color='#0ea5e9', edgecolors='black')

#trendline
z = np.polyfit(df['absences'], df['G3'], 1)
p = np.poly1d(z)
plt.plot(df['absences'], p(df['absences']), color='#e11d48', linewidth='2', linestyle='--')

plt.title('Impact of Absences on Final Grade', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Total Days of Absent', fontsize=12)
plt.ylabel('Final Grade (0 - 20)', fontsize=12)
plt.tight_layout()
plt.savefig('absences_vs_grades.png', dpi=300)
plt.show()

# Chart 2: The Study Time Advantage (Bar Chart)
plt.figure(figsize=(9, 6))
avg_grades = df.groupby('studytime')['G3'].mean()
bars = plt.bar(avg_grades.index, avg_grades.values, color='#2dd4bf', edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 1), ha='center', va='bottom', fontweight='bold')

plt.title('Average Final Grade by Study Time Category', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Weekly Study Time (1 = lowest,  = Highest)', fontsize=12)
plt.ylabel('Average Final Grade', fontsize=12)
plt.xticks(avg_grades.index)
plt.tight_layout()
plt.savefig('studytime_vs_grades.png', dpi=300)
plt.show()

# Chart 3: Internet Acces Disparity (Boxplot)
plt.figure(figsize=(8, 6))
data_to_plot = [df[df['internet'] == 0]['G3'], df[df['internet'] == 1]['G3']]

box = plt.boxplot(data_to_plot, patch_artist=True, labels=['No Internet', 'Has Internet'])

colors = ['#f87171', '#34d399']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for median in box['medians']:
    median.set(color='black', linewidth=2)

plt.title('Distribution of Grades Based on Home Internet Access', fontsize=16, fontweight='bold', pad=15)
plt.ylabel('Final Grade (0 - 20)', fontsize=12)
plt.tight_layout()
plt.savefig('internet_boxplot.png', dpi=300)
plt.show()
