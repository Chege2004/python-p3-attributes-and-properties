#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="John Doe", job="Admin"):
        # Use the property setters
        self.name = name  # Invokes the name setter
        self.job = job  # Invokes the job setter

    # Property for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case and store
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None  # Set to None if the name is invalid

    # Property for job
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = None  # Set to None if the job is invalid
