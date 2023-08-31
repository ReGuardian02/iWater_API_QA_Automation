from enum import  Enum

class Genders(Enum):
    female = "Female"
    male = "Male"

class Statuses(Enum):
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"

class UserErrors(Enum):
    WRONG_EMAIL = "Email must contain @"