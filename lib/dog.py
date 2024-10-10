#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle",
    "French Bulldog", "Pug", "Pointer"
]

class Dog:
    def __init__(self, name="Dog", breed="Mastiff"):
        # Use the property setters
        self.name = name  # This will invoke the name setter
        self.breed = breed  # This will invoke the breed setter

    # Property for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Dog"  # Set to default name if invalid

    # Property for breed
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Mastiff"  # Set to default breed if invalid
