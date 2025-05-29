def get_bills(bills) -> None:
    for k in bills:
        try:
            user_input = float(input(f"Input {k} bill amount or input 0 to skip >> "))
        except ValueError:
            print("Error, not a number!")
        except:
            print("Something went wrong!")
        else:
            bill: float = user_input
            bills.update({k: bill})


def calculate_bills(amount) -> None:
    total: float = 0.0
    for k, v in bills.items():
        bills[k] = float(v)
    for k, v in bills.items():
        divided: float = bills[k] / amount
        bills.update({k: divided})
        total += divided
    for k, v in bills.items():
        print(k.capitalize(), v)
    print("-----------------")
    print(f"Total for each person: {round(total, 2)}")


bills = {
    "rent": 0.0,
    "electricity": 0.0,
    "water": 0.0,
    "internet": 0.0,
    "home insurance": 0.0,
    "heating": 0.0
}

amount = int(input("Input roommate amount >> "))
get_bills(bills)
print("-----------------")
calculate_bills(amount)