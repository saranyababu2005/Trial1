from locust import User, between, SequentialTaskSet, task


class SeqTasks(SequentialTaskSet):

    @task(5)
    def task1(self):
        print("task1")

    @task(1)
    def task2(self):
        print("task2")


class MyUser(User):

    wait_time = between(1,2)
    tasks = [SeqTasks]