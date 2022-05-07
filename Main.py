import datetime
import os

class Person:
    def __init__(self, gender, name, surname, birth_date, death_date, father, mother, children):
        self.gender = gender
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.death_date = death_date
        self.father = father
        self.mother = mother
        self.mother = mother
        self.children = children

tree = []

def print_tree():
    print()
    for p in tree:
        print(p.gender, p.name, p.surname, p.birth_date,
                p.death_date, p.mother, p.father, p.children)

def print_person(p):
    print()
    print(tree[p].gender, tree[p].name, tree[p].surname, tree[p].birth_date,
            tree[p].death_date, tree[p].mother, tree[p].father, tree[p].children)

def find_person(name, surname):
    for p in tree: # Check the person in tree or not
        if name == p.name and surname == p.surname:
            return tree.index(p)
    
    return -1

def find_relationship(fn, fs, sn, ss):
    is_first = False
    is_second = False

    for p in tree:
        if p.name == fn and p.surname == fs:
            first = p
            is_first = True
        elif p.name == sn and p.surname == ss:
            second = p
            is_second = True
    
    if is_first == False and is_second == False:
        print(fn, fs, "and", sn, ss, "are not in the tree.")
        return -1
    if is_first == False:
        print(fn, fs, "is not in the tree.")
        return -1
    if is_second == False:
        print(sn, ss, "is not in the tree.")
        return -1

    if first.name == second.father:
        return 'babası'
    elif first.name == second.mother:
        return 'annesi'
    elif first.father == second.name or first.mother == second.name:
        if first.gender == 'M': return 'oğlu'
        else: return 'kızı'
    elif first.father == second.father and first.mother == second.mother:
        if first.birth_date < second.birth_date:
            if first.gender == 'M': return 'abisi'
            else: return 'ablası'
        else:
            if first.gender == 'M': return 'erkek kardeşi'
            else: return 'kız kardeşi'
    
    for p in tree:
        if first.father == p.father and first.mother == p.mother and p.gender == 'M' and second.father == p.name:
            if first.gender == 'M': return 'amcası'
            else: return 'halası'
        elif first.father == p.father and first.mother == p.mother and p.gender == 'F' and second.mother == p.name:
            if first.gender == 'M': return 'dayısı'
            else: return 'teyzesi'
        
        if first.father == p.name or first.mother == p.name:
            for p1 in tree:
                if p.father == p1.father and p.mother == p1.mother and p1.name == second.name and p1.surname == second.surname:
                    return 'yeğeni'
                    
    return -2

def generate_tree():
    # 1
    tree.append(Person('M', 'Ali', 'Yılmaz', datetime.date(1927,1,1), datetime.date(1997,1,1), None, None, 4))
    tree.append(Person('F', 'Ayşe', 'Yılmaz', datetime.date(1930,1,1), datetime.date(2000,1,1), None, None,  4))
    # 2
    tree.append(Person('M', 'Fatih', 'Çetin', datetime.date(1952,1,1), datetime.date(2020,1,1), 'Ramiz', 'Fatma', 2))
    tree.append(Person('F', 'Burcu', 'Çetin', datetime.date(1955,1,1), None, 'Ali', 'Ayşe', 2))
    # 3
    tree.append(Person('M', 'Berk', 'Çetin', datetime.date(1980,1,1), None, 'Fatih', 'Burcu', 0))
    tree.append(Person('F', 'Sıla', 'Çetin', datetime.date(1985,1,1), None, 'Fatih', 'Burcu', 0))
    # 2
    tree.append(Person('M', 'Tolga', 'Yılmaz', datetime.date(1960,1,1), None, 'Ali', 'Ayşe', 2))
    tree.append(Person('F', 'Gözde', 'Yılmaz', datetime.date(1963,1,1), None, 'İdris', 'Sultan', 2))
    # 3
    tree.append(Person('M', 'Murat', 'Yılmaz', datetime.date(1988,1,1), None, 'Tolga', 'Gözde', 0))
    tree.append(Person('F', 'Ebru', 'Yılmaz', datetime.date(1993,1,1), None, 'Tolga', 'Gözde', 0))
    # 2
    tree.append(Person('M', 'Mehmet', 'Demir', datetime.date(1962,1,1), None, 'Ömer', 'Nazife', 2))
    tree.append(Person('F', 'Beyza', 'Demir', datetime.date(1965,1,1), None, 'Ali', 'Ayşe', 2))
    # 3
    tree.append(Person('M', 'Yasin', 'Demir', datetime.date(1990,1,1), None, 'Mehmet', 'Beyza', 0))
    tree.append(Person('F', 'Tuğba', 'Demir', datetime.date(1995,1,1), None, 'Mehmet', 'Beyza', 0))
    # 2
    tree.append(Person('M', 'Osman', 'Yılmaz', datetime.date(1970,1,1), None, 'Ali', 'Ayşe', 0))

def user_interface():
    os.system('CLS')
    answer = 0
    while True:
        print('\n1) Add a person to tree.' + '\n2) Update a person in tree.'
                + '\n3) Print the tree.' + '\n4) Ask relationship between 2 people.' '\n5) Exit')
        answer = int(input("Answer(NO): "))

        if answer == 1:
            gender = input('\nGender(M/F): ')
            name = input('Name: ')
            surname = input('Surname: ')

            entry = input('Birth Date(yyyy-mm-dd): ')
            year, month, day = map(int, entry.split('-'))
            birth_date = datetime.date(year,month,day)

            entry = input('Death Date(yyyy-mm-dd): ')
            year, month, day = map(int, entry.split('-'))
            death_date = datetime.date(year,month,day)

            father = input('Father(name): ')
            mother = input('Mother(name): ')
            children = input('Children(number): ')

            tree.append(Person(gender, name, surname, birth_date, death_date, father, mother, children))

        elif answer == 2:
            print('\nEnter name & surname of the person you want to update:')
            name = input('\tName: ')
            surname = input('\tSurname: ')

            p_idx = find_person(name, surname)

            if p_idx == -1:
                print('The person you entered is not in the tree.')
                continue

            print_person(p_idx)

            print("\nUpdate person:")
            tree[p_idx].gender = input('\tGender(M/F): ')
            tree[p_idx].name = input('\tName: ')
            tree[p_idx].surname = input('\tSurname: ')
            
            entry = input('Birth Date(yyyy-mm-dd): ')
            year, month, day = map(int, entry.split('-'))
            tree[p_idx].birth_date = datetime.date(year,month,day)
            
            entry = input('Death Date(yyyy-mm-dd): ')
            year, month, day = map(int, entry.split('-'))
            tree[p_idx].death_date = datetime.date(year,month,day)
            
            tree[p_idx].father = input('\tFather(name): ')
            tree[p_idx].mother = input('\tMother(name): ')
            tree[p_idx].children = input('\tChildren(number): ')

        elif answer == 3:
            print_tree()

        elif answer == 4:
            print('\nFirst Person')
            f_name = input('\tName: ')
            f_surname = input('\tSurname: ')

            print('Second Person')
            s_name = input('\tName: ')
            s_surname = input('\tSurname: ')

            rel = find_relationship(f_name, f_surname, s_name, s_surname)

            if rel == -1:
                continue
            elif rel == -2:
                print("There is no relationship between them.")
            else:
                print(f_name, f_surname + ',', s_name, s_surname + '\'s', rel + '.')

        elif answer == 5:
            print('\nExited.\n')
            break

def main():
    generate_tree()

    user_interface()

if __name__ == "__main__":
    main()