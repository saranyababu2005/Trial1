from locust import User, task, between


class MyUser(User):
    wait_time = between(1,2)

    @task
    def task1(self):
        print("My task1")

    @task
    def task2(self):
        print("My task2")
