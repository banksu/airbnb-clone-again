import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command creates many rooms"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many rooms do you want to create.",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        print(room_types, all_user)
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_user),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(10, 5000),
                "guests": lambda x: random.randint(1, 5),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photo = seeder.execute()
        created_clean = flatten(list(created_photo.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            potato = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 20)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=potato,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )
                # many to many fields
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    potato.amenity.add(a)
            for b in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    potato.facility.add(b)
            for c in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    potato.house_rule.add(c)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
