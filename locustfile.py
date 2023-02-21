from locust import events

from CommonLib.EventInfluxHandlers import InfluxHandlerEvents
from Tasks.TaskSet1 import Task1
from Users.NormalUser import GeneralUser

from CommonLib.EventHandlers import EventHandlers

class Group1(GeneralUser):
    tasks = [Task1]


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("first one")
    InfluxHandlerEvents.init_influx_client()