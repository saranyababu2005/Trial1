from locust import User, between, TaskSet, task


class Tasks(TaskSet):

    @task(5)
    def task1(self):
        print("My task1")

    @task(1)
    def task2(self):
        print("My task2")

class MyUser(User):
    wait_time = between(1,2)
    tasks = [Tasks]
