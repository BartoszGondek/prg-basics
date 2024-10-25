def time_string(hours, minutes, time_format):
    if time_format not in [12,24]:
        return 'Invalid format'
    if hours < 0 or hours > 23 and minutes < 0 or minutes > 59:
        return 'Invalid time'
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    else:
        period = 'AM' if hours < 12 else 'PM'
        hour12 = hours % 12 
        hour12 = hour12 if hour12 !=0 else 12 
        return f"{hour12}:{minutes:02} {period}"
    
hours = int(input('Enter hour from 0 to 23: ' ))
minutes = int(input('Enter minutes from 0 to 59: ' ))
time_format = int(input('Enter time format 24 or 12: ' ))
time = time_string(hours, minutes, time_format)
print(time)

    


    