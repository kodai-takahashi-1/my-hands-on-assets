from datetime import datetime
import sys, os
import math
from zoneinfo import ZoneInfo



def process_user_data(user_name,user_age: int,department: str) -> str:     
    output_str = "Name:"+user_name+", Age:"+str(user_age)+", Dept:"+department
    print( output_str )
    
    if user_age > 20 and department != "sales":
        temp_val = user_age * 2

    today = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    print("Today's date is:", today)
    return output_str

processed_info = process_user_data("Alice", 25, 'HR')
