

'''

**Warning** The function must be called life_in_weeks for the tests to pass. Also the output must have the same punctuation and spelling as the example. Including the full stop!
    
    



Example Input

56



Example Output

You have 1768 weeks left.



How to test your code and see your output?



Udemy coding exercises do not have a console, so you cannot use input() . You will need to call your function with hard-coded values like so:



def life_in_weeks(age):
  # your code here


# Call your function with hard coded values
life_in_weeks(12)


def life_in_weeks(age):

    converted = age * 52
    print("Age converted in weeks:", converted)
    print("You have",4680-converted,"weeks left.")



life_in_weeks(4)
'''


def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(f"love score between devang and kohli is {score}")


calculate_love_score("Devang Sabbarwal", "Virat Kohli")



























