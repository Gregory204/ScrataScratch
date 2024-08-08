# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()
airbnb_search_details.groupby(['property_type', 'city'])['bedrooms', 'bathrooms'].mean().reset_index().rename(columns={
'bedrooms' : 'bedrooms_avg', 
'bathrooms' : 'bathrooms_avg'})
