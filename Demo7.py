from locust import events
from locust import User, between, SequentialTaskSet, task

@events.test_start.add_listener
def before_all(**kwargs):
    print("Executing before all")


@events.test_stop.add_listener
def after_all(**kwargs):
    print("Executing after all")

class Task1(SequentialTaskSet):
    @task
    def task1(self):
        print("My task1")

    @task
    def task2(self):
        print("My task2")

    @task
    def quit_from_taskset1(self):
        self.interrupt()

    def on_start(self):
        print("Before Task")

    def on_stop(self):
        print("After Task")


class MyUser(User):
    wait_time = between(1,2)
    tasks= [Task1]

    def on_start(self):
        print("Before User")

    def on_stop(self):
        print("After User")

