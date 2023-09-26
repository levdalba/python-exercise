def make_calendar(year, start_day, layout_option):
    months = [
        ('January', 31),
        ('February', 28),
        ('March', 31),
        ('April', 30),
        ('May', 31),
        ('June', 30),
        ('July', 31),
        ('August', 31),
        ('September', 30),
        ('October', 31),
        ('November', 30),
        ('December', 31)
    ]

    week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

    start_pos = week.index(start_day)

    if is_leap(year):
        months[1] = ('February', 29)

    if layout_option == "1*12":
        calendar_layout = [months]
    elif layout_option == "2*6":
        calendar_layout = [months[i:i + 1]
                           for i in range(0, len(months))]
    elif layout_option == "3*4":
        calendar_layout = [months[i:i+3] for i in range(0, len(months), 3)]
    else:
        print("Invalid layout option.")
        return

    for row in calendar_layout:
        for month, days in row:
            if layout_option == "1*12":
                print(f'{month} {year}'.center(20, ' '),)
                print(''.join(['{0:<3}'.format(w) for w in week]))
                print('{0:<3}'.format('') * start_pos, end='')
            elif layout_option == "2*6":
                print(f'{month}{year}'.format(20, ' '),)
                print(''.join(['{0:<3}'.format(w) for w in week]))
                print('{0:<3}'.format('') * start_pos, end='')
            elif layout_option == "3*4":
                print(f'{month} {year}'.center(20, ' '),)
                print(''.join(['{0:<3}'.format(w) for w in week]))
                print('{0:<3}'.format('') * start_pos, end='')
            for day in range(1, days + 1):
                print('{0:<3}'.format(day), end='')
                start_pos += 1
                if start_pos == 7:
                    print()
                    start_pos = 0
            print('\n')


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    yr = int(input('Enter Year: '))
    strtday = input(
        'Enter start day of the year (Mo, Tu, We, Th, Fr, Sa, Su(default=mo)): ') or 'Mo'
    layout_option = input('Enter layout option (1*12, 2*6, 3*4): ')
    make_calendar(yr, strtday, layout_option)
