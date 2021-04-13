def calc(summa, rate, month):
    if (month == 0):
        return summa
    return calc(summa, rate, month - 1) * (1 + rate / (12 * 100))


summa_user = float(input("Enter your deposit amount: "))

rate_user = float(input("Enter the interest rate: "))
amount_user = float(input("Enter your total amount you want to accrue: "))
time = 12

amount = calc(summa_user, rate_user, time)
time = (amount_user / amount) / 12
interest = amount - summa_user

print(f"You will accrue this in {round(time, 2)} months")
