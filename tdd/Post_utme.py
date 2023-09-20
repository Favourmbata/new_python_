class Post_utme():
    def __init__(self):
        self.result = 0

    def get_price(self, number_of_copies):
        if 1 <= number_of_copies <= 4:
            self.result = 2000
        elif 5 <= number_of_copies <= 9:
            self.result = 1800
        elif 10 <= number_of_copies <= 29:
            self.result = 1600
        elif 30 <= number_of_copies <= 49:
            self.result = 1500
        elif 50 <= number_of_copies <= 99:
            self.result = 1300
        elif 100 <= number_of_copies <= 199:
            self.result = 1200
        elif 200 <= number_of_copies <= 499:
            self.result = 1100
        else:
            self.result = 1000
        return self.result
