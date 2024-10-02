from datetime import datetime, timedelta

def day_of_year_to_date(day, year):
    try:
        date = datetime(year, 1, 1) + timedelta(days=day - 1)
        formatted_date = date.strftime("%d %B, %Y")
        
        return formatted_date
    except ValueError as e:
        return f"Error: {e}"
    
day_number = 256
year = 2021
output_date = day_of_year_to_date(day_number, year)
print(output_date)  
