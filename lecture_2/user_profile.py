

import datetime

current_date_time = datetime.datetime.now()

current_year = current_date_time.year
THIS_YEAR = current_year


def generate_profile(age: int):

    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid Age"


def run_profile_build():

    print("Welcome!")

    user_name = input("Input your name: ")


    while True:
        birth_year_str = input("Input birth year: ")
        try:
            birth_year = int(birth_year_str)
            current_age = int(THIS_YEAR - birth_year)
            break
        except ValueError:
            print("Error% birth year must be an integer")


    hobbies = []
    print("\n Input your hobbies:")
    while True:
        hobby_input = input("Enter a favorite hobby or type 'stop' to finish: ").strip()
        if hobby_input.lower() == "stop":
            break

        if hobby_input:
            hobbies.append(hobby_input)

    life_stage = generate_profile(current_age)

    user_profile = {
        "name": user_name,
        "birth_year": birth_year,
        "age": current_age,
        "stage": life_stage,
        "hobbies": hobbies
    }


    print("=" * 40)
    print(f" Name: {user_profile['name']}")
    #print(f" **:** {user_profile['birth_year']}")
    print(f" Current age for {THIS_YEAR}: {user_profile['age']} years")
    print(f" Life stage: {user_profile['stage']}")

    print("\n Hobbies:")
    if not user_profile["hobbies"]:
        print(" You didn't list any hobbies")
    else:
        hobby_count = len(user_profile["hobbies"])
        print(f" Favorite Hobbies ({hobby_count}):")
        for hobby in user_profile["hobbies"]:
            print(f"- {hobby}")




# Запуск программы
if __name__ == "__main__":
    run_profile_build()