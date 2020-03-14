class Person:

    count = 0
    current_year = 2019
    is_christmas = False

    def check_name(full_name):
        if not isinstance(full_name, str):
            raise TypeError
        if full_name.split != ' ':
            full_name = 'Guy Incognito'


    def check_year(year):
        if not isinstance(year, int):
            raise TypeError
        if not year >= 0:
            raise ValueError

    def __init__(self, full_name, year):

        Person.counter += 1
        self.id = Person.counter

        Person.check_name(full_name)

        self.full_name = full_name

        Person.check_year(year)

        self.year = year

    def get_full_name(self, full_name):
        Person.check_name(new_full_name)
        self.full_name = new_full_name
