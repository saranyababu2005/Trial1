import os

from locust import events
import socket
import csv


class EventHandlers:

    hostname = socket.gethostname()
    success_req_list = []
    fail_req_list = []

    @staticmethod
    @events.request.add_listener
    def my_request_handler(request_type, name, response_time, response_length, response,
                           context, exception, start_time, url, **kwargs):
        if exception:
            print("fail")
            EventHandlers.fail_req_list.append([EventHandlers.hostname, request_type, name, response_time,
                                                response_length,[ exception, "FAIL"]])
        else:
            print("pass")
            EventHandlers.success_req_list.append([EventHandlers.hostname, request_type, name, response_time,
                                                  response_length, "PASS"])

    @staticmethod
    def save_success_stats():
        with open(os.getcwd() +"/success_req_stats.csv", "wt") as csv_file:
            writer = csv.writer(csv_file)
            for value in EventHandlers.success_req_list:
                writer.writerow(value)

    @staticmethod
    def save_failure_stats():
        with open(os.getcwd() +"/failure_req_stats.csv", "wt") as csv_file:
            writer = csv.writer(csv_file)
            for value in EventHandlers.fail_req_list:
                writer.writerow(value)

    @staticmethod
    @events.quitting.add_listener
    def exit_handlers(**kwargs):
        EventHandlers.save_success_stats()
        EventHandlers.save_failure_stats()












