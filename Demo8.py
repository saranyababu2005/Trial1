from locust import HttpUser, between, SequentialTaskSet, task


class MyTasks(SequentialTaskSet):
    @task
    def view_booking(self):
        # response = self.client.get("booking/5839")
        # print(response.text)
        with self.client.get("booking/3038", catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(resp.text)
                print(resp.status_code)


class MyUser(HttpUser):
    wait_time=between(1,2)
    tasks =[MyTasks]
