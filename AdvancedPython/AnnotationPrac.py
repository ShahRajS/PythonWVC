def calculate_pay(hours: float, rate: float) -> float:
    return hours * rate


def get_input() -> [float, float]:
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))
    return hours, rate


def print_pay(pay: float) -> None:
    print(f"The total pay is: {pay:.2f}")


def main():
    hours, rate = get_input()
    pay = calculate_pay(hours, rate)
    print_pay(pay)

    print(calculate_pay.__annotations__)
    print(get_input.__annotations__)
    print(print_pay.__annotations__)


if __name__ == "__main__":
    main()
