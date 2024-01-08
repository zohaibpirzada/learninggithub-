def user_name(firstname , middlename, lastname):
    firstname = input("what is your first name? ")
    middlename = input("what is your middle name? ")
    lastname = input("what is your last name? ")
    if middlename:
        print(f"hellow, {firstname} {middlename} {lastname}")
    else:
        print(f"hellow, {firstname} {lastname}")

user_name(firstname,middlename,lastname)