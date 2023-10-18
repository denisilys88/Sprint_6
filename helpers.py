from faker import Faker


class Helpers:

    @staticmethod
    def fake_data():
        faker = Faker('ru_RU')
        user_data = [faker.first_name(), faker.last_name()]
        return user_data
