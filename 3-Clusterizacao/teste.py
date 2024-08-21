import datetime
import locale

def get_current_day():
    # Set locale to C.utf8 as pt_BR.utf8 is not available
    locale.setlocale(locale.LC_TIME, 'C.utf8')
    
    brazil_timezone = datetime.timezone(datetime.timedelta(hours=-3))  # Brazil timezone is UTC-3
    current_time = datetime.datetime.now(datetime.timezone.utc).astimezone(brazil_timezone)
    current_day = current_time.strftime("%A")  # Format the current time as the day of the week in English
    
    # Map English day names to Brazilian Portuguese
    day_mapping = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    
    # Convert the day name to Brazilian Portuguese
    current_day_pt = day_mapping.get(current_day, current_day)
    return current_day_pt

# Test the function
print(get_current_day()) 

def calculate_distance_two_points():
    # Calculate the distance between two points
    x1, y1 = 1, 2  # coordinates of the first point
    x2, y2 = 3, 4  # coordinates of the second point

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance