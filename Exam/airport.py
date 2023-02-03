import datetime
import json
import re
import os.path
import sys
import action_airport


def main():
    if len(sys.argv) != 2:  # checking if the length of argument is 2
        print("The airplane data does not exist")
        exit(0)

    json_filename = sys.argv[1] # the first argument is the file name

    airplane_list = action_airport.load_file_data(json_filename)  # loading the json file

    quit = False

    while not quit:
        try:
            print("Add_airplane (a), List Airplanes(n), Find Airplanes(f), Remove Airplane (r), Quit(q):")
            option = input("Enter an action:")

            if option == "a":
                # Add a note
                action_airport.add_airplane(airplane_list) # invoking add book method for adding

                action_airport.save_file_data(json_filename, airplane_list)  # saving the json file

            elif option == "r":
                action_airport.remove_airplane(airplane_list)  # invoking the delete book method
                action_airport.save_file_data(json_filename, airplane_list)

            elif option == "n":
                action_airport.display_airplane(airplane_list)  # invoking the summary of the book method
                action_airport.save_file_data(json_filename, airplane_list)

            elif option == "f":
                action_airport.find_and_display(airplane_list)  # invoking the search by title method
                action_airport.save_file_data(json_filename, airplane_list)

            elif option == "q":
                print("Quitting airplane")  # quitting
                quit = True
            else:
                print("Invalid option try again")
        except ValueError as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
