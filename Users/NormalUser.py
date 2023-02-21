from locust import HttpUser, between

from Data.LoadUser import AddData


class GeneralUser(HttpUser):
    wait_time =between(1,2)
    abstract =True

    def on_start(self):
        self.bookingData = AddData.get_BookingOrder()
        print(self.bookingData)

    def give_booking_data(self):
        return self.bookingData


