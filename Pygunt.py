import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import datetime

# Define the project phases and their timelines
phases = {
    "Prepare Base Tech, Infra, and CI Pipeline": ["2024-02-01", "2024-02-07"],
    "Prepare Base Website Features": ["2024-02-08", "2024-02-14"],
    "Benchmark System & Evaluate Resource Usage": ["2024-02-22", "2024-02-28"],
    "Outline for New Project Documentation Styles": ["2024-02-22", "2024-02-28"],
}

# Create a DataFrame
df = pd.DataFrame(list(phases.items()), columns=['Phase', 'Date'])
df['Start'], df['Finish'] = zip(*df['Date'])

# Convert date strings to datetime objects
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

# Remove the original 'Date' column
df.drop('Date', axis=1, inplace=True)

# Create a Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))
labels = []
for i, task in enumerate(df.iterrows()):
    task = task[1]
    start = task['Start']
    finish = task['Finish']
    ax.barh(task['Phase'], (finish - start).days, left=start, height=0.3)
    labels.append(task['Phase'])

# Set labels and title
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel('Date')
ax.set_title('Gantt Chart for Website Development')

# Format the date display
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

plt.grid(True)
plt.tight_layout()
plt.show()

