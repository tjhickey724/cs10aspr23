def main():
    years = float(input("Enter your age in years: "))
    months = years_to_months(years)
    print("you are",months,"months old")

def years_to_months(y):
    m = y*12
    print('here')
    return(m)

main()
