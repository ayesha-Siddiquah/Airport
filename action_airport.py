import datetime
import json
import re
import os.path
import sys
import string


def add_airplane(airplane_list):
    aircraftt_numm = input("Air Craft Number")
    if re.search("^[A-Z]{5}[0-9]+$", aircraftt_numm) is None:  # validating the title
        raise ValueError("The Aircraft Number is invalid")
    aircraftt = input("Mention aircraft:")
    if re.search("^[A-Za-z0-9 ]+$", aircraftt) is None:  # validating the author
        raise ValueError("The Aircraft is invalid")
    airlinee = input("Input the airline:")
    if re.search("^[A-Za-z0-9 ]+$", airlinee) is None:
        raise ValueError("The Airline is invalid")
    capacityy = input("capacity:")
    if re.search("^[0-9]+$", capacityy) is None:  # validating the isbn
        raise ValueError("The capacity must be a valid integer")

    # checking whether the ISBN is being repeated or not
    for note in airplane_list:
        if note['aircraft_num'] == aircraftt_numm:
            raise ValueError("Airplane already exists at the Airport” instead.")

    airplane_record = {"aircraft_num": aircraftt_numm,
            "aircraft": aircraftt,
            "airline": airlinee,
            "capacity": capacityy
            }

    airplane_list.append(airplane_record)


def remove_airplane(airplane_list):

    aircraftt_numm = input(":")

    if re.search("^[0-9]{4,18}$", aircraftt_numm) is None:  # validating the isbn
        raise ValueError("isbn should contain 4 to 18 digits ")
    else:
        removing = False

        for airplane_record in range(len(airplane_list)):
            if airplane_list[airplane_record]['aircraft_num'] == aircraftt_numm:
                removing = True
                del airplane_list[airplane_record]  # deleting the record with the particular isbn
                print(f"Airplane {aircraftt_numm} departed from airport")
                break

        if not removing:
            print(f" No airplane {aircraftt_numm} found")


def display_airplane(airplane_list):

 #List all airplane_list
    if len(airplane_list) == 0:
        print("There is no inventory summary to display")
    else:
        for airplane_record in airplane_list:
            print(f" {airplane_record['aircraft_num']} is a {airplane_record['aircraft']} from {airplane_record['airline']} with a capacity of {airplane_record['capacity']} passengers")


def find_and_display(airplane_list):

    search_text_by_aircraft_num = input("Keyword for aircraft_num:")

    matches_found = False

    for airplane_record in airplane_list:
        match = re.search(search_text_by_aircraft_num, airplane_record['aircraft_num'])  # finding the search by title
        if match:
            print(f" {airplane_record['aircraft_num']} is a {airplane_record['aircraft']} from {airplane_record['airline']} with a capacity of {airplane_record['capacity']} passengers")
            matches_found = True

    if not matches_found:
        print("No airplane found.")


def load_file_data(filename):

    if os.path.isfile(filename):
        fh = open(filename, "r")  # opening the file to read
        json_str = fh.read()
        airplane_list = json.loads(json_str) # loads json data in the string
        fh.close()
    else:
        print("No inventory exist yet.")
        airplane_list = []  # empty list of inventory

    return airplane_list


def save_file_data(filename, airplane_list):
    fh = open(filename, "w")  # writing the data onto the file specified
    json_str = json.dumps(airplane_list, indent=4)
    fh.write(json_str)
    fh.close()
