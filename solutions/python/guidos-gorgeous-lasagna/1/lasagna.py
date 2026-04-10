#Solution to Guido's Gorgeous Lasagna

#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining, in minutes.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the
    lasagna still needs to bake based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

#TODO: Define the 'preparation_time_in_minutes()' function below.

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
    :param number_of_layers: int = number of lasagna layers.
    :return: int * the time it takes to prepare a lasagna layer (2 minutes) from 'PREPARATION_TIME'
    Function that take the number of lasagna layer as an argument and returns the time, in minutes,it will take to prepare
    that lasagna, before baking.
    """
    return number_of_layers * PREPARATION_TIME

#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the elapsed time in the kitchen in minutes.
    
    :param number_of_layers: int = number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: (int * int * the time it takes to prepare a lasagna layer (2 minutes) from 'PREPARATION_TIME') + (int -
    remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME').
    
    Function that takes the number of lasagna layers and the time elapsed baking the lasagna as arguments, and returns the
    total elapsed time in the kitchen, in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# TODO: Remember to go back and add docstrings to all your functions
