def get_day_of_week(S: str, K: int) -> str:
     """
     Returns the day of the week for a given start day and # 
     of days afterwards.

     Parameters:
     S (str): The start day.
     K (int): # of days after start day.

     Returns:
     str: The day of the week after K days.
     """
    
     daysOfTheWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    
     beginningDayIndex = daysOfTheWeek.index(S)

     # calculate # of days after the start of the week
     # remainder represents the days within the 7 day range
     indexOfDayK = (beginningDayIndex + K) % 7 
     
     return daysOfTheWeek[indexOfDayK] # return the day at that index

# 4 weeks pass by and the extra day = +1
print(get_day_of_week("mon", 29))