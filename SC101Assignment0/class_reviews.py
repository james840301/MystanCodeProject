"""
File: class_reviews.py
Name:James
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1  # The number the user inputs to stop entering new score


def main():
    choose_class = input('Which class? ')
    if choose_class == str(EXIT):
        print('No class scores were entered')
    else:
        # Initial values
        count1 = 0
        count2 = 0
        max1 = 0
        max2 = 0
        min1 = 0
        min2 = 0
        total1 = 0
        total2 = 0
        while True:
            if choose_class == str(EXIT):
                break
            if choose_class.upper() == 'SC001':
                score = int(input('Score: '))
                count1 += 1
                if count1 == 1:
                    max1 = score
                    min1 = score
                    total1 = score
                else:
                    if max1 < score:
                        max1 = score
                    elif min1 > score:
                        min1 = score
                    total1 += score
            elif choose_class.upper() == 'SC101':
                score = int(input('Score: '))
                count2 += 1
                if count2 == 1:
                    max2 = score
                    min2 = score
                    total2 = score
                else:
                    if max2 < score:
                        max2 = score
                    elif min2 > score:
                        min2 = score
                    total2 += score
            choose_class = input('Which class? ').upper()
        # Show the results
        print('===========SC001===========')
        if total1 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(max1))
            print('Min (001): ' + str(min1))
            print('Avg (001): ' + str(total1 / count1))

        print('===========SC101===========')
        if total2 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max2))
            print('Min (101): ' + str(min2))
            print('Avg (101): ' + str(total2 / count2))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
