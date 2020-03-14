class Person:
    counter = 0
    current_year = 2019
    is_christmas = False

    def check_name(full_name):
        if not isinstance(full_name, str) or not full_name.split(' '):
            full_name = 'Guy Incognito'


    def check_year(year):
        if year <= 0:
            year = 2000

    def __init__(self,full_name, year):
        Person.check_name(full_name)
        Person.check_year(year)
        self.full_name = full_name
        self.year = year

        Person.counter += 1
        self.id = Person.counter


    def __str__(self):
        return '#{}: {} {}'.format(self.id, self.full_name, self.year)

    def get_age(self):
        return (Person.current_year - self.year)

    def get_friendly_name(self):
        self.full_name.split(' ')
        first_name = self.full_name[0]
        if Person.is_christmas == True:
            return print(first_name, chr(0x1F384))
        return first_name

    def celebrate_new_year():
        Person.current_year += 1
        Person.is_christmas = True

    def go_back_to_work():
        Person.is_christmas = False



p1 = Person('Homer Simpson', 1982)
print(Person.counter)
print('#{}: {} {}'.format(p1.id, p1.full_name, p1.year))

p2 = Person('Maggie Simpson', 2017)
print(Person.counter)
print('#{}: {} {}'.format(p2.id, p2.full_name, p2.year))

p3 = Person('Burns', 0)
print(Person.counter)
print('#{}: {} {}'.format(p3.id, p3.full_name, p3.year))

Person.celebrate_new_year()
print(Person.current_year)
print(Person.is_christmas)

print(Person.get_age(p2))
print(Person.get_friendly_name(p2))

Person.celebrate_new_year()
print(Person.current_year)
print(Person.is_christmas)

Person.go_back_to_work()
print(Person.current_year)
print(Person.is_christmas)
