from enum import Enum
import simplejson as json
from utils import get_config_file
from constants import (
    KG_TO_LB,
    IN_TO_CM,
    SEDENTARY_FACTOR,
    LIGHT_FACTOR,
    MODERATE_FACTOR,
    VERY_FACTOR,
    EXTRA_FACTOR,
    PRO_FACTOR,
)


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class Activity(Enum):
    SEDENTARY = 0
    LIGHT = 1
    MODERATE = 2
    VERY = 3
    EXTRA = 4
    PRO = 5


class User:
    def __init__(self, name, age, weight, height, activity, sex=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.activity = activity
        self.sex = sex
        self.protein = 0
        self.fats = 0
        self.carbs = 0

    def kg_weight(self):
        return int(self.weight) / KG_TO_LB

    def cm_height(self):
        return int(self.height) * IN_TO_CM

    def print_info(self):
        print(
            f"age: {self.age} === weight: {self.weight} === height: {self.height} === activity: {self.activity} === sex: {self.sex}"
        )
        print(
            f"Protein: {self.protein:.2f}  === Carbs: {self.carbs}  === Fat: {self.fats} "
        )


def new_user():
    name = input("Enter name -> ")
    print(
        f"Welcome, {name}! Let's gather some info about you so we can\ngive you the most accurate results!"
    )
    age = input("Age -> ")
    weight = input("Weight (lbs) -> ")
    height = input("Height (inches) -> ")
    user_input_sex = input("Sex (M, F, or N (other/prefer not to say)) -> ")
    match user_input_sex:
        case "M" | "m":
            sex = Gender.MALE
        case "F" | "f":
            sex = Gender.FEMALE
        case _:
            sex = Gender.OTHER
    print(
        "What's your activity level? Enter the number corresponding to your activity level."
    )
    print("Sedentary=0, Light=1, Moderate=2, Very=3, Extra=4, Professional=5")
    activity = input("Activity -> ")
    print(f"Thanks, {name}! Let's calculate your results!")
    new_user = User(name, age, weight, height, activity, sex)
    save_user(new_user)
    return new_user


def calculate(user):
    bmr = _calc_bmr(user)
    calories = bmr * get_activity_factor(user.activity)
    print(f"Calories = {calories:.2f}")
    print(f"protein(10%) = {.1 * calories}")
    user.protein = 1 * user.kg_weight()


def get_activity_factor(activity):
    match Activity(activity):
        case Activity.SEDENTARY:
            return SEDENTARY_FACTOR
        case Activity.LIGHT:
            return LIGHT_FACTOR
        case Activity.MODERATE:
            return MODERATE_FACTOR
        case Activity.VERY:
            return VERY_FACTOR
        case Activity.EXTRA:
            return EXTRA_FACTOR
        case Activity.PRO:
            return PRO_FACTOR
        case _:
            raise ValueError("Invalid activity level.")


def _calc_bmr(user):
    if user.sex == Gender.FEMALE:
        return (
            655.1
            + (9.563 * user.kg_weight())
            + (1.850 * user.cm_height())
            - (4.676 * float(user.age))
        )
    else:
        return (
            66.5
            + (13.75 * user.kg_weight())
            + (5.003 * user.cm_height())
            - (6.75 * float(user.age))
        )


def encode_user(obj):
    if isinstance(obj, User):
        return [obj.name, obj.age, obj.weight, obj.height, obj.activity, obj.sex]
    if isinstance(obj, Gender):
        return obj.name
    raise TypeError(repr(obj) + " is not Json serializable")


def save_user(user):
    try:
        file_path = get_config_file()
        with open(file_path, "w+") as f:
            json.dump(user, f, default=encode_user)
    except FileNotFoundError:
        print("Error: .mmcc_config.json was not found.")
    return None


def find_user():
    try:
        file_path = get_config_file()
        with open(file_path) as f:
            data = json.load(f)
        if data != None:
            user = User(*data)
            user.activity = int(user.activity)
            return user
    except FileNotFoundError:
        print("Error: .mmcc_config.json was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from file")
    return None
