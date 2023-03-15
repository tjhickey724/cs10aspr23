# Converts degrees Fahrenheit to Celsius.
def f_to_c(degrees_f):
    degrees_c = 5.0 / 9.0 * (degrees_f - 32)
    return degrees_c

def main():
    c = f_to_c(98.6)
    print('98.6F=',c,'C')

main()

