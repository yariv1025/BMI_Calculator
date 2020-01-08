from src.bmi_calculator import *
from src.bubble_sort import *


def main():
    # BMI Calc
    body_mass = input("Please Enter body mass:")
    body_height = input("Please Enter body height:")

    print("your BMI category is : " + bmi_calc(body_mass, body_height))

    # Bubble sort
    array = []
    size = int(input("Please enter size of array :"))
    for i in range(size):
        array.append(input("Please enter element number " + str(i + 1) + "/" + str(size) + " to the array"))

    print("The sorted array is :\n" + bubble_sort(array))


if __name__ == "__main__":
    main()
