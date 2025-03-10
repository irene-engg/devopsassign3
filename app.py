def area_of_square(side_length):
    """
    Calculate the area of a square given the side length.
    :param side_length: int or float, length of one side of the square
    :return: float, area of the square
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length must be a positive number")

    return round(side_length * side_length, 2)


if __name__ == "__main__":
    try:
        side = float(input("Enter the side length of the square: "))
        print(f"The area of the square is: {area_of_square(side)}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")
