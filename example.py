
# RED STEPS : Write the restand run it ( it should fail)

# "Joe" --> "Welcom joe"

# Green STEPS : Write the logic so that the test succeeds

# Refactor STEPS : Improve you code

def greet_person(name):
    # capitalised_name = name.capitalize()
    # greeting_message = f"Welcom {capitalised_name}"
    # return greeting_message

    return f'Welcome {name.capitalize()}'

def can_drink_alcohol(age):
    try:
        int(age)
    except ValueError:
        raise TypeError('You need to enter a number!')
    return age >= 21