
def birthday():
    birthdays={"Ana" : "3/7/1999", "Marija": "17/01/1991",
    "Stefan": "11/08/1896",
    "Aleksandar": "25/10/1992"}
    return birthdays

if __name__ == "__main__":
    birthdays=birthday()
    print("Dobredojdovte do recniot za rodendeni. Nie gi znaeme rodendenite na:")
    print("\n".join(birthdays.keys()))
    print("Koj rodenden e potrebno da se prebara?")
    user = input()

    birthday = birthdays[user]
    print(f"Rodendenot na {user} e na {birthday}")