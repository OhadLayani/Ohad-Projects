def timeConversion(s):
    arr = list(s)
    if arr[8] == 'P':
        hour = int(arr[0] + arr[1])
        if hour != 12:
            hour = (hour + 12) % 24  # Adding 12 and taking modulo 24 to handle the case where it becomes 24
        arr[0:2] = str(hour).zfill(2)
    elif arr[8] == 'A' and arr[0] == '1' and arr[1] == '2':
        arr[0:2] = '00'  # Special case for 12:00:00AM
    arr = arr[:-2]
    result_string = ''.join(arr)
    return result_string

if __name__ == '__main__':
    s = "12:45:54PM"
    result = timeConversion(s)
    print(result)