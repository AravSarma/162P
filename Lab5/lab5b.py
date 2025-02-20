from person import Person

def main():
    person = Person("Reanica", 22)
    print(f"Original Name: {person.get_name()}")
    print(f"Original Age: {person.get_age()}")
    person.set_name("Arav")
    person.set_age(21)
    print(f"New Name: {person.get_name()}")
    print(f"New Age: {person.get_age()}")

if __name__ == "__main__":
    main()


