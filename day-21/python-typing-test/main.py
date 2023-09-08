from time import *
import random as r


def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
            error = error+1
    return error


def speed_time(time_s, time_e, words):
    actual_t = time_e - time_s
    time_round = round(actual_t, 2)
    speed = len(words) / time_round

    return round(speed) * 60


test = ["As I sit in my room late at night, staring at the computer screen",
        "This is my third Python project, I am really loving it, this paragraph",
        "I really love Python, it is greate to work in it."]

test_1 = r.choice(test)
print("     ***** Typing Speed *****")
print(test_1)
print()
print()
time_1 = time()
test_input = input("Test Your Typing speed:\n")
time_2 = time()
print("Speed: ", speed_time(time_1, time_2, test_input), "words/min")
print("Mistakes: ", mistake(test_1, test_input), "mistakes are found in the test")
