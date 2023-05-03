#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Owner, Pet

fake = Faker()

with app.app_context():

    Pet.query.delete()
    Owner.query.delete()

    owners = [Owner(name=fake.name()) for n in range(50)]

    db.session.add_all(owners)

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    pets = [Pet(name=fake.first_name(), species=rc(
        species), owner=rc(owners)) for n in range(100)]

    db.session.add_all(pets)
    db.session.commit()
