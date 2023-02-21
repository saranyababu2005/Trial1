import csv
import json
import os


class AddData:

    booking_list = []

    @staticmethod
    def add_data():
        with open(os.getcwd()+"/Data/BookingDetails.json",'r') as booking_details:
            data_reader = json.load(booking_details)
        print(data_reader)
        for item in data_reader:
            AddData.booking_list.append(item)
            print(item)

    @staticmethod
    def get_BookingOrder():
        if len(AddData.booking_list)<1:
            AddData.add_data()
        return AddData.booking_list.pop()