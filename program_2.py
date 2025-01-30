def get_valid_integer(prompt, min_value, max_value):
    formatted_prompt = prompt.ljust(20)

    while True:
        try:
            user_input = input(formatted_prompt)
            user_input = user_input.capitalize()
            value = int(user_input)

            if min_value <= value <= max_value:
                return value
            else:
                print(f"{prompt.split('(')[0]} must be between {min_value} and {max_value}.")
        except ValueError:
            print(f"{prompt.split('(')[0]} must be between {min_value} and {max_value}.")

year = get_valid_integer("Year (2000-2999):", 2000, 2999)
month = get_valid_integer("Month (1-12):", 1, 12)

print(f"Valid year: {year}, valid month: {month}")