from itertools import islice

def get_bills(bills) -> None:
    for k, v in islice(bills.items(), len(bills)-2, len(bills)):
        try:
            user_input = float(input(f"Input {k} bill amount >> "))
            if user_input == 0:
                continue
        except ValueError:
            print("Error, not a number!")
        except:
            print("Something went wrong!")
        else:
            bill: float = user_input
            bills.update({k: bill})


def calculate_bills() -> None:
    total: float = 0.0
    for k, v in bills.items():
        bills[k] = float(v)
    for k, v in bills.items():
        divided: float = bills[k] / 2
        bills.update({k: divided})
        total += divided
    for k, v in bills.items():
        print(f"{k.capitalize()} payment is {v}")
    print("\n")
    print(f"Total payment: {round(total, 2)}")


bills = {
    "rent": 1200.0,
    "internet": 24.95,
    "home insurance": 30.50,
    "electricity": 0.0,
    "water": 0.0
}

get_bills(bills)
print("-----------------")
calculate_bills()