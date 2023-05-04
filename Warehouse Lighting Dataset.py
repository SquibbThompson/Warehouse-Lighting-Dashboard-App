import pandas as pd
import panel as pn

pn.extension()

# Create a Pandas dataframe with the information
df = pd.DataFrame({
    'Color': ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'White'],
    'Atomic Name and Number': ['Neon (10)', 'Helium (2)', 'Sodium (11)', 'Neon (10)', 'Mercury (80)', 'Argon (18)', 'Xenon (54)'],
    'Semiconductor Catalyst': ['Gallium (Ga)', 'Gallium (Ga)', 'Indium (In)', 'Indium (In)', 'Indium (In)', 'Indium (In)', 'None (RGB)'],
    'Properties': ['Efficient, low-power consumption, bright, warm tone', 'Bright, high efficiency, good color rendition', 'Bright, efficient, good color rendition, suitable for outdoors', 'Bright, efficient, good color rendition, suitable for outdoors', 'High brightness, cool tone, suitable for displays', 'High brightness, good color rendition, suitable for mood lighting', 'Versatile, can create a range of color temperatures, high efficiency']
})

# Create a Panel dataframe widget
df_widget = pn.widgets.DataFrame(df)

# Display the widget
df_widget.show()


