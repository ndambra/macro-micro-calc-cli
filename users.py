from enum import Enum
import simplejson as json
from utils import get_config_file

# TODO: figure out how to work with enums and json to print better
class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

Activity = Enum("Activity", ["SEDENTARY"])


class User:
    def __init__(self, name, age, weight, height, activity, sex=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.activity = activity
        self.sex = sex

    def calc(self):
        print("Protein:  === Carbs: === Fat: ")
    
    def print_info(self):
        print(f"age: {self.age} === weight: {self.weight} === height: {self.height} === activity: {self.activity} === sex: {self.sex}")


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

def encode_user(obj):
    if isinstance(obj, User):
        return [obj.name, obj.age, obj.weight, obj.height, obj.activity, obj.sex]
    if isinstance(obj, Gender):
        return obj.name
    raise TypeError(repr(obj) + " is not Json serializable")

def save_user(user):
    try:
        file_path = get_config_file()
        with open(file_path, "w+")  as f:
            json.dump(user, f, default=encode_user)
    except FileNotFoundError:
        print("Error: .mmcc_config.json was not found.")
    return None

def find_user():
    try:
        file_path = get_config_file()
        with open(file_path)  as f:
            data = json.load(f)
        if data != None:
            user = User(*data)
            return user
    except FileNotFoundError:
        print("Error: .mmcc_config.json was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from file")
    return None


