import string
import random
import sys

# Get user input and make sure it's an int.
# n is the length of the desired string (output).
try:
    n = int(sys.argv[1])
except Exception as e:
    print("Error:", e)
    print("Invalid input. Please enter an integer.")
    sys.exit()


def main():

    # Make sure user input is at least 5 or larger (rest of the code works on this assumption).
    if n < 5:
        print("Invalid input. Please enter an integer larger than, or equal to 5.")
        sys.exit()

    # Here we calculate the number of characters of each type that will exist in the final string.
    # At least 20% of the string will consist of lowercase, 20% of uppercase, 10% of digits, and 20% punctuation.
    # However float(n) * 0.2 results in a float, and the variables have to be integers. Which means we ROUND DOWN
    # using int(n). So 1.8 becomes 1. This means that the variables added up, will be LESS than n, and we account for
    # this using the num_of_remainder variable, which is simply n minus all nums.
    num_of_lowercase = int(float(n) * 0.2)
    num_of_uppercase = int(float(n) * 0.2)
    num_of_digits = int(float(n) * 0.1)
    num_of_punctuation = int(float(n) * 0.2)
    num_of_remainder = int(n) - num_of_lowercase - num_of_uppercase - num_of_digits - num_of_punctuation

    # mixed is a shuffled list of lowercase, uppercase, digits, and punctuation characters.
    mixed = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    random.shuffle(mixed)

    chars_dict = {
        1: {"counter": num_of_lowercase, "chars": string.ascii_lowercase},
        2: {"counter": num_of_uppercase, "chars": string.ascii_uppercase},
        3: {"counter": num_of_digits, "chars": string.digits},
        4: {"counter": num_of_punctuation, "chars": string.punctuation},
        5: {"counter": num_of_remainder, "chars": "".join(mixed)}
    }

    # Loop n number of times to generate the string.
    s = ""
    i = 0
    while i < n:
        random_choice = random.randint(1, 5)

        # This code block ensures all counters eventually reach 0.
        if chars_dict[random_choice]["counter"] == 0:
            while True:
                random_choice = random.randint(1, 5)
                if chars_dict[random_choice]["counter"] != 0:
                    break

        # Decrement counter, and add the random selection from chars_dict[random_choice]["chars"] to s.
        chars_dict[random_choice]["counter"] -= 1
        s += random.choice(chars_dict[random_choice]["chars"])
        i += 1

    print(s)


if __name__ == "__main__":
    main()
