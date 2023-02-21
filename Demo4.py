from locust import User, between, SequentialTaskSet, task


class Taskset1(SequentialTaskSet):
    @task
    def task1(self):
        print("My task1")

    @task
    def task2(self):
        print("My task2")


class Taskset2(SequentialTaskSet):
    @task
    def task3(self):
        print("My task3")

    @task
    def task4(self):
        print("My task4")

class MyUser(User):
    wait_time = between(1,2)
    tasks=[Taskset1,Taskset2]
