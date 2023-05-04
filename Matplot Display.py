import matplotlib.pyplot as plt

data = {
    'Color': ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'White'],
    'Optimal Time': ['10am-2pm', '8am-10am', '2pm-4pm', '9am-5pm', '8pm-12am', '6pm-12am', '12am-12am']
}


# Create a function to convert time range to hours
def time_range_to_hours(time_range):
    start, end = time_range.split('-')
    start_hour = int(start[:-2]) + (12 if start[-2:] == 'pm' else 0)
    end_hour = int(end[:-2]) + (12 if end[-2:] == 'pm' else 0)

    # Account for time wrapping around midnight
    if end_hour <= start_hour:
        end_hour += 24

    return end_hour - start_hour


# Calculate the duration for each color
durations = [time_range_to_hours(time_range) for time_range in data['Optimal Time']]

# Colors matching the labels
colors = data['Color']

# Create the pie chart
plt.pie(durations, labels=data['Color'], colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.title('Color Timeframe Ratio')

# Show the pie chart
plt.show()

