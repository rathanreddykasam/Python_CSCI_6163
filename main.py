prompt = "Amount:".ljust(20)

while True:
    try:  # to catch error if user enters any letter
        sales_amount = float((input(prompt)))
        if sales_amount > 0:
            print('Sales Amount:', sales_amount)
            break  #this breaks the loop
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Amount must be a number")