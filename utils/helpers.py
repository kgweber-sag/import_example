import pandas as pd
from faker import Faker
fake = Faker()

def create_example_dataframe(len=4):
    data = {
        'name': [fake.first_name() for x in range(len)],
        'location': [fake.city() for x in range(len)],
        'dob': [fake.date_of_birth(minimum_age=18, maximum_age=65) for x in range(len)],
    }
    return pd.DataFrame(data)