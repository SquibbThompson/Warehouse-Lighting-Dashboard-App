import pandas as pd
import panel as pn
import seaborn as sns
import matplotlib.pyplot as plt
pn.extension()


# Create a Pandas dataframe with the information
df = pd.DataFrame({
    'Color': ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'White'],
    'Atomic Name and Number': ['Neon (10)', 'Helium (2)', 'Sodium (11)', 'Neon (10)', 'Mercury (80)', 'Argon (18)',
                               'Xenon (54)'],
    'Semiconductor Catalyst': ['Gallium (Ga)', 'Gallium (Ga)', 'Indium (In)', 'Indium (In)', 'Indium (In)',
                               'Indium (In)', 'None (RGB)'],
    'Properties': ['Efficient, '
                   'low-power consumption, '
                   'bright, '
                   'warm tone',
                   'Bright, '
                   'high efficiency, '
                   'good color rendition',
                   'Bright, '
                   'efficient, '
                   'good color rendition, '
                   'suitable for outdoors',
                   'Bright, efficient, '
                   'good color rendition, '
                   'suitable for outdoors',
                   'High brightness, '
                   'cool tone, suitable for displays',
                   'High brightness, good color rendition, '
                   'suitable for mood lighting',
                   'Versatile, '
                   'can create a range of color temperatures, '
                   'high efficiency'],
    'Optimal Time' : ['10pm-2am', '8pm-10pm', '2am-4am', '9pm-5am', '8am-12pm', '6am-12pm', '12pm-12pm'],
    'Start Time' : [22, 20, 2, 21, 8, 6, 12],
    'End Time': [2, 22, 4, 5, 12, 12, 12]})

# Define a Panel function that creates the widget
def show_dataframe(df):
    return pn.widgets.DataFrame(df, fit_columns=True, width=1600, font_size='24pt')

# create a function to show the metadata widget
def show_metadata(df):
        atomic_summary = {
            'Neon (10)': 'Neon is a noble gas with the atomic number 10. It is colorless, odorless, and inert in most conditions. [Wikipedia](https://en.wikipedia.org/wiki/Neon)',
            'Helium (2)': 'Helium is a noble gas with the atomic number 2. It is the second lightest element and has various applications, including cooling for MRI machines. [Wikipedia](https://en.wikipedia.org/wiki/Helium)',
            'Sodium (11)': 'Sodium is an alkali metal with the atomic number 11. It is highly reactive and is commonly found in compounds such as table salt. [Wikipedia](https://en.wikipedia.org/wiki/Sodium)',
            'Mercury (80)': 'Mercury is a heavy metal with the atomic number 80. It is the only metal that is liquid at room temperature and has various industrial applications. [Wikipedia](https://en.wikipedia.org/wiki/Mercury_(element))',
            'Argon (18)': 'Argon is a noble gas with the atomic number 18. It is colorless, odorless, and mostly inert, often used as a shielding gas in welding. [Wikipedia](https://en.wikipedia.org/wiki/Argon)',
            'Xenon (54)': 'Xenon is a noble gas with the atomic number 54. It is colorless, odorless, and has a variety of applications, including in lighting and medical imaging. [Wikipedia](https://en.wikipedia.org/wiki/Xenon)',
        }

        metadata = [
            f"**Color:** {row.Color}  \n**Atomic Name and Number:** {row['Atomic Name and Number']}  \n**Semiconductor Catalyst:** {row['Semiconductor Catalyst']}  \n**Properties:** {row.Properties}  \n**Elemental Summary:** {atomic_summary[row['Atomic Name and Number']]}"
            for _, row in df.iterrows()]
        return pn.Column(metadata)
###********

df['Wrapped End Time'] = df['End Time'].apply(lambda x: x if x >= 12 else x + 24)

# Update the show_visualization function
def show_visualization(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Wrapped End Time', y='Color', data=df, orient='h', ax=ax, palette=df['Color'].tolist())
    sns.barplot(x='Start Time', y='Color', data=df, orient='h', ax=ax, color='white', edgecolor='black')
    plt.title('Optimal Time by Color')
    plt.xlabel('Optimal Time (24 Hr Clock)')
    plt.ylabel('Color')
    plt.xlim(0, 36)  # Changed the upper limit to 36 to accommodate wrapped times
    ax.set_xticks(list(range(0, 37, 6)))  # Set custom x-axis ticks to show wrapped times
    ax.set_xticklabels([f"{i % 24}" for i in range(0, 37, 6)])  # Set custom x-axis labels for wrapped times
    plt.tight_layout()
    return pn.pane.Matplotlib(fig, tight=True)

class DashboardState:
    def __init__(self, df):
        self.df = df
        self.viz_pane = pn.pane.Matplotlib()

    def update_visualization(self, event):
        new_df = self.df.copy()
        for color, (start, end) in self.color_time_sliders.items():
            new_df.loc[new_df['Color'] == color, 'Start Time'] = start.value
            new_df.loc[new_df['Color'] == color, 'End Time'] = end.value
            new_df.loc[new_df['Color'] == color, 'Wrapped End Time'] = end.value if end.value >= 12 else end.value + 24
        self.viz_pane.object = self.show_visualization(new_df).object



# Initialize the dashboard state
state = DashboardState(df)

# Create interactive sliders for each color
color_time_sliders = {}
for color in df['Color'].unique():
    start_time_slider = pn.widgets.IntSlider(name=f"{color} Start Time", start=0, end=24, step=1)
    end_time_slider = pn.widgets.IntSlider(name=f"{color} End Time", start=0, end=24, step=1)
    start_time_slider.param.watch(state.update_visualization, 'value')
    end_time_slider.param.watch(state.update_visualization, 'value')
    color_time_sliders[color] = (start_time_slider, end_time_slider)

state.color_time_sliders = color_time_sliders

sliders = pn.Column(*[slider for sliders in color_time_sliders.values() for slider in sliders])

    ##*********

# Create the widgets
df_widget = show_dataframe(df)
metadata_widget = show_metadata(df)
viz_widget = show_visualization(df)

# Create a Panel dashboard layout
dashboard = pn.Tabs(
    ("Dataframe", show_dataframe(df)),
    ("Metadata", show_metadata(df)),
    ("Visualization", viz_widget)
)

# Combine the widgets into one app
app = pn.Tabs(("Dataframe", df_widget), ("Metadata", metadata_widget))

# Run app
app.servable()

# Display the dashboard
dashboard.show()