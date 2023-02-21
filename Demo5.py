from locust import User, between, SequentialTaskSet, task


class Taskset1(SequentialTaskSet):
    @task
    def task1(self):
        print("My task1")

    @task
    def task2(self):
        print("My task2")

    @task
    def quit_from_taskset1(self):
        self.interrupt()


class Taskset2(SequentialTaskSet):
    @task
    def task3(self):
        print("My task3")

    @task
    def task4(self):
        print("My task4")

    @task
    def quit_from_taskset2(self):
        self.interrupt()

class MyUser(User):
    wait_time = between(1,2)
    tasks=[Taskset1,Taskset2]
