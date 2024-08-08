select city, property_type, AVG (bathrooms) AS bathrooms_avg, AVG(bedrooms) AS bedrooms_avg
from airbnb_search_details
GROUP BY city, property_type
ORDER BY city
