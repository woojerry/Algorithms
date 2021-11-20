def timeConversion(s):
    # Write your code here
    s = '07:05:45PM'
    time, minute, sec_with_format = s.split(":")
    print(time)
    sec, form = sec_with_format[0:2], sec_with_format[2:]

    if time == "12":
        if form == "AM":
            time = "00"
            print(time)
    else:
        if form == "PM":
            time = str(int(time) + 12)

    return f'{time}:{minute}:{sec}'


print(timeConversion("07:05:45PM"))
print(timeConversion("12:01:00AM"))
