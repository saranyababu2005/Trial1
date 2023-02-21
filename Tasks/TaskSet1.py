from locust import SequentialTaskSet, task


class Task1(SequentialTaskSet):

    @task
    def task1(self):
        bookingData = self.user.give_booking_data()
        print(bookingData)
        auth_headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = self.client.post('/booking', headers=auth_headers, json=bookingData)
        response_json = response.json()
        self.booking_id = response_json['bookingid']

    @task
    def getBookingDetails(self):
        response = self.client.get('/booking/{}'.format(self.booking_id))
        print(response.text)