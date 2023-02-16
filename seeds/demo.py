from flask_seeder import Seeder, Faker, generator
from app.models import UserProfile

class DemoSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create UserProfile objects
        faker = Faker(
            cls=UserProfile,
            init={
                "first_name":  generator.Name(),
                "last_name": generator.Name(),
                "username": generator.String("620\d{6}"),
                "password": "Password123"
            }
        )

        # create 2 Users
        for user in faker.create(2):
            print("Adding user: %s" % user)
            self.db.session.add(user)