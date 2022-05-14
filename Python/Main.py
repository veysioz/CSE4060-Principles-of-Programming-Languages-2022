import datetime
import os
import json

class Person:
    def __init__(self, gender, name, surname, birth_date, death_date, father, mother, generation):
        self.gender = gender
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.death_date = death_date
        self.father = father
        self.mother = mother
        self.spouse = None
        self.children = []
        self.generation = generation

tree = []

def print_tree():
    for p in tree:
        print(p.gender, p.name, p.surname, p.birth_date, p.death_date, end=" ")
        
        if p.father == None: print(None, end=" ")
        else: print(p.father.name, end=" ")

        if p.mother == None: print(None, end=" ")
        else: print(p.mother.name, end=" ")

        if p.spouse == None: print(None, end=" ")
        else: print(p.spouse.name, end=" ")

        if p.children == None: print(None, end=" ")
        else:
            for child in p.children:
                print(child.name, end=" ")
        
        print(p.generation)

def cocuk(p):
    cocuk = []
    if p != None:
        for i in p.children:
            cocuk.append(i)
    return cocuk

def kardes(p):
    kardes = []
    if p != None:
        for i in cocuk(p.father):
            if p != i: kardes.append(i)
    return kardes

def ogul(p):
    ogul = []
    for i in cocuk(p):
        if i.gender == 'M': ogul.append(i)
    return ogul

def kiz(p):
    kiz = []
    for i in cocuk(p):
        if i.gender == 'F': kiz.append(i)
    return kiz

def erkek_kardes(p):
    erkek_kardes = []
    for i in ogul(p.father):
        if i.birth_date >= p.birth_date: erkek_kardes.append(i)
    return erkek_kardes

def kiz_kardes(p):
    kiz_kardes = []
    for i in kiz(p.father):
        if i.birth_date >= p.birth_date: kiz_kardes.append(i)
    return kiz_kardes

def abi(p):
    abi = []
    for i in ogul(p.father):
        if i.birth_date < p.birth_date: abi.append(i)
    return abi

def abla(p):
    abla = []
    for i in kiz(p.father):
        if i.birth_date < p.birth_date: abla.append(i)
    return abla

def amca(p):
    amca = []
    for i in kardes(p.father):
        if i.gender == 'M':
            amca.append(i)
    return amca

def hala(p):
    hala = []
    for i in kardes(p.father):
        if i.gender == 'F':
            hala.append(i)
    return hala

def dayi(p):
    dayi = []
    for i in kardes(p.mother):
        if i.gender == 'M':
            dayi.append(i)
    return dayi

def teyze(p):
    teyze = []
    for i in kardes(p.mother):
        if i.gender == 'F':
            teyze.append(i)
    return teyze

def yegen(p):
    yegen = []
    for i in cocuk(p.father):
        for j in cocuk(i): yegen.append(j)
    return yegen

def kuzen(p):
    kuzen = []
    for i in kardes(p.father):
        for j in cocuk(i): kuzen.append(j)
    for i in kardes(p.mother):
        for j in cocuk(i): kuzen.append(j)
    return kuzen

def eniste(p):
    eniste = []
    for i in hala(p): eniste.append(i.spouse)
    for i in teyze(p): eniste.append(i.spouse)
    for i in kardes(p):
        if i.gender == 'F': eniste.append(i.spouse)
    return eniste

def yenge(p):
    yenge = []
    for i in dayi(p): yenge.append(i.spouse)
    for i in amca(p): yenge.append(i.spouse)
    for i in kardes(p):
        if i.gender == 'M': yenge.append(i.spouse)
    return yenge

def kayinvalide(p):
    if p.spouse != None: return p.spouse.mother

def kayinpeder(p):
    if p.spouse != None: return p.spouse.father

def damat(p):
    damat = []
    for i in kiz(p): damat.append(i.spouse)
    return damat

def gelin(p):
    gelin = []
    for i in ogul(p): gelin.append(i.spouse)
    return gelin

def baldiz(p):
    baldiz = []
    if p.gender == 'M':
        for i in kardes(p.spouse):
            if i.gender == 'F': baldiz.append(i)
    return baldiz

def bacanak(p):
    bacanak = []
    for i in baldiz(p): bacanak.append(i.spouse)
    return bacanak

def kayinbirader(p):
    kayinbirader = []
    for i in kardes(p.spouse):
        if i.gender == 'M': kayinbirader.append(i)
    return kayinbirader

def elti(p):
    elti = []
    if p.gender == 'F':
        for i in kardes(p.spouse):
            if i.gender == 'M': elti.append(i.spouse)
    return elti

def find_relationship(p1, p2):
    if p1 == p2.father: return 'babası'
    if p1 == p2.mother: return 'annesi'
    if p1 == p2.spouse: return 'eşi'
    if p1 in ogul(p2): return 'oğlu'
    if p1 in kiz(p2): return 'kızı'
    if p1 in erkek_kardes(p2): return 'erkek kardeşi'
    if p1 in kiz_kardes(p2): return 'kız kardeşi'
    if p1 in abi(p2): return 'abisi'
    if p1 in abla(p2): return 'ablası'
    if p1 in amca(p2): return 'amcası'
    if p1 in hala(p2): return 'halası'
    if p1 in dayi(p2): return 'dayısı'
    if p1 in teyze(p2): return 'teyzesi'
    if p1 in yegen(p2): return 'yeğeni'
    if p1 in kuzen(p2): return 'kuzeni'
    if p1 in eniste(p2): return 'eniştesi'
    if p1 in yenge(p2): return 'yengesi'
    if p1 == kayinvalide(p2): return 'kayınvalidesi'
    if p1 == kayinpeder(p2): return 'kayınpederi'
    if p1 in damat(p2): return 'damadı'
    if p1 in gelin(p2): return 'gelini'
    if p1 in baldiz(p2): return 'baldızı'
    if p1 in bacanak(p2): return 'bacanağı'
    if p1 in kayinbirader(p2): return 'kayınbiraderi'
    if p1 in elti(p2): return 'eltisi'

    return 'nothing'

def add_spouse(p1, p2):
    tree.append(p2)
    p1.spouse, p2.spouse = p2, p1

def add_child(p1, p2, p3):
    tree.append(p3)
    p1.children.append(p3)
    p2.children.append(p3)

def generate_tree():
    with open('input.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    
    for i in range(1, len(data)+1):
        gender = data[str(i)]["gender"]
        name = data[str(i)]["name"]
        surname = data[str(i)]["surname"]
        birth_date = list(map(int, data[str(i)]["birth_date"].split(',')))

        if data[str(i)]["death_date"] == None: death_date = None
        else: death_date = list(map(int, data[str(i)]["death_date"].split(',')))

        if data[str(i)]["father"] == None: father = None
        else: father = tree[int(data[str(i)]["father"])-1]

        if data[str(i)]["mother"] == None: mother = None
        else: mother = tree[int(data[str(i)]["mother"])-1]

        if data[str(i)]["spouse"] == None: spouse = None
        else: spouse = int(data[str(i)]["spouse"]) - 1

        generation = int(data[str(i)]["generation"])

        if death_date == None:
            p = Person(gender, name, surname, datetime.date(birth_date[0],birth_date[1],birth_date[2]), None, father, mother, generation)
        else:
            p = Person(gender, name, surname, datetime.date(birth_date[0],birth_date[1],birth_date[2]),
                        datetime.date(death_date[0],death_date[1],death_date[2]), father, mother, generation)

        if spouse != None: add_spouse(tree[spouse], p)
        elif father != None and mother != None: add_child(father, mother, p)
        else: tree.append(p)

    file.close()

def user_interface():
    os.system('CLS')
    answer = 0
    while True:
        print('\n1) Add a person to tree.' + '\n2) Update a person in tree.'
                + '\n3) Print the tree.' + '\n4) Ask relationship between 2 people.'
                + '\n5) Check marriage under the age of 18.' + '\n6) Exit')
        answer = int(input('Answer(NO): '))

        if answer == 1:
            print('\n1) Child.' + '\n2) Spouse')
            answer = int(input('Answer(NO): '))

            if answer == 1:
                print('\nFather')
                father_name = input('\tName: ')
                father_surname = input('\tSurname: ')
                print('Mother')
                mother_name = input('\tName: ')
                mother_surname = input('\tSurname: ')

                father, mother = None, None
                for i in tree:
                    if i.name == father_name and i.surname == father_surname:
                        spouse = i.spouse
                        if spouse.name == mother_name and spouse.surname == mother_surname:
                            father, mother = i, spouse
                            break
                
                if father == None:
                    print('There is no such couple in the tree.')
                    continue
                if father.death_date != None:
                    print('Father is dead.')
                    continue
                if mother.death_date != None:
                    print('Mother is dead.')
                    continue
                    
                print('Child')
                gender = input('\tGender(M/F): ')
                name = input('\tName: ')
                surname = input('\tSurname: ')
                date = input('\tBirth Date(yyyy-mm-dd): ')
                year, month, day = map(int, date.split('-'))
                birth_date = datetime.date(year,month,day)
                alive = input('\tIs the child alive?(yes/no): ')
                
                if alive == 'yes':
                    death_date = None
                else:
                    date = input('\tDeath Date(yyyy-mm-dd): ')
                    year, month, day = map(int, date.split('-'))
                    death_date = datetime.date(year,month,day)

                add_child(father, mother, Person(gender, name, surname, birth_date, death_date, father, mother, father.generation + 1))
                print('The child is added to tree.')
            
            elif answer == 2:
                print('\nWhose Spouse')
                spouse_name = input('\tName: ')
                spouse_surname = input('\tSurname: ')

                spouse = None
                for i in tree:
                    if i.name == spouse_name and i.surname == spouse_surname:
                        spouse = i
                        break
                
                if spouse == None:
                    print('There is no one with this name in the tree.')
                    continue
                if spouse.spouse != None:
                    print('This person is already married.')
                    continue

                print('Spouse')
                gender = input('\tGender(M/F): ')
                name = input('\tName: ')
                surname = input('\tSurname: ')
                date = input('\tBirth Date(yyyy-mm-dd): ')
                year, month, day = map(int, date.split('-'))
                birth_date = datetime.date(year,month,day)
                alive = input('\tIs the spouse alive?(yes/no): ')
                
                if alive == 'yes':
                    death_date = None
                else:
                    date = input('\tDeath Date(yyyy-mm-dd): ')
                    year, month, day = map(int, date.split('-'))
                    death_date = datetime.date(year,month,day)

                add_spouse(spouse, Person(gender, name, surname, birth_date, death_date, None, None, spouse.generation))
                print('The spouse is added to tree.')
        
        elif answer == 2:
            print('\nWho to update')
            update_name = input('\tName: ')
            update_surname = input('\tSurname: ')

            update = None
            for i in tree:
                if i.name == update_name and i.surname == update_surname:
                    update = i
                    break
            
            if update == None:
                print('There is no one with this name in the tree.')
                continue

            print('New Informations')
            update.gender = input('\tGender(M/F): ')
            update.name = input('\tName: ')
            update.surname = input('\tSurname: ')
            update.date = input('\tBirth Date(yyyy-mm-dd): ')
            year, month, day = map(int, date.split('-'))
            birth_date = datetime.date(year,month,day)
            alive = input('\tIs the spouse alive?(yes/no): ')
            
            if alive == 'yes':
                update.death_date = None
            else:
                date = input('\tDeath Date(yyyy-mm-dd): ')
                year, month, day = map(int, date.split('-'))
                update.death_date = datetime.date(year,month,day)
            
            print('The person is updated.')

        elif answer == 3:
            print()
            print_tree()

        elif answer == 4:
            n1 = input('First Person\'s Name: ')
            n2 = input('Second Person\'s Name: ')

            p1s, p2s = [], []
            for p in tree:
                if p.name == n1:
                    p1s.append(p)
                if p.name == n2:
                    p2s.append(p)
            
            if len(p1s) == 0:
                print('There is no one named', n1, 'in the tree.')
            if len(p2s) == 0:
                print('There is no one named', n2, 'in the tree.')
            if len(p1s) == 0 or len(p2s) == 0:
                continue

            for p1 in p1s:
                for p2 in p2s:
                    rel = find_relationship(p1, p2)
                    print(p1.name, p1.surname + ',', p2.name, p2.surname + '\'s', rel + '.')
        
        elif answer == 5:
            print()
            check = True
            
            for i in tree:
                if i.spouse != None:
                    age = datetime.datetime.now().year - i.spouse.birth_date.year

                    if age < 18:
                        check = False
                        print(i.spouse.name, i.spouse.surname + ':', age)
                        i_age = datetime.datetime.now().year - i.birth_date.year
                        print(i.name, i.surname + ':', i_age)
                        break
            
            if check: print('There is no marriage under the age of 18.')
        
        elif answer == 6:
            print('\nExited.\n')
            break

        else:
            print('\nPlease enter one of the numbers in the menu.')

def main():
    generate_tree()
    
    user_interface()

if __name__ == "__main__":
    main()