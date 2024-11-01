from dataclasses import replace
from faker.generator import random
from file_operations import VERSION
import file_operations
from faker import Faker
import random
import os


os.makedirs('./all_results',0o755,exist_ok=True)
fake = Faker("ru_RU")
skills = ['Кислотный взгляд',"Тайный побег","Ледяной выстрел","Огненный заряд",
          "Стремительный прыжок","Электрический выстрел","Ледяной удар","Стремительный удар"]
runic_skills = []
symbols = {'а': 'а͠',
               'б': 'б̋',
               'в': 'в͒͠',
               'г': 'г͒͠',
               'д': 'д̋',
               'е': 'е͠',
               'ё': 'ё͒͠',
               'ж': 'ж͒',
               'з': 'з̋̋͠',
               'и': 'и',
               'й': 'й͒͠',
               'к': 'к̋̋',
               'л': 'л̋͠',
               'м': 'м͒͠',
               'н': 'н͒',
               'о': 'о̋',
               'п': 'п̋͠',
               'р': 'р̋͠',
               'с': 'с͒',
               'т': 'т͒',
               'у': 'у͒͠',
               'ф': 'ф̋̋͠',
               'х': 'х͒͠',
               'ц': 'ц̋',
               'ч': 'ч̋͠',
               'ш': 'ш͒͠',
               'щ': 'щ̋',
               'ъ': 'ъ̋͠',
               'ы': 'ы̋͠',
               'ь': 'ь̋',
               'э': 'э͒͠͠',
               'ю': 'ю̋͠',
               'я': 'я̋',
               'А': 'А͠',
               'Б': 'Б̋',
               'В': 'В͒͠',
               'Г': 'Г͒͠',
               'Д': 'Д̋',
               'Е': 'Е',
               'Ё': 'Ё͒͠',
               'Ж': 'Ж͒',
               'З': 'З̋̋͠',
               'И': 'И',
               'Й': 'Й͒͠',
               'К': 'К̋̋',
               'Л': 'Л̋͠',
               'М': 'М͒͠',
               'Н': 'Н͒',
               'О': 'О̋',
               'П': 'П̋͠',
               'Р': 'Р̋͠',
               'С': 'С͒',
               'Т': 'Т͒',
               'У': 'У͒͠',
               'Ф': 'Ф̋̋͠',
               'Х': 'Х͒͠',
               'Ц': 'Ц̋',
               'Ч': 'Ч̋͠',
               'Ш': 'Ш͒͠',
               'Щ': 'Щ̋',
               'Ъ': 'Ъ̋͠',
               'Ы': 'Ы̋͠',
               'Ь': 'Ь̋',
               'Э': 'Э͒͠͠',
               'Ю': 'Ю̋͠',
               'Я': 'Я̋',
               ' ': ' '}

def main():
    for i in skills:
        runic_skill = i
        for key, value in symbols.items():
            runic_skill = runic_skill.replace(key, value)
            runic_skills.append(runic_skill)
    for render_template in range (10):
        n = 0
        while n < 10:
            skill_3 = random.sample(runic_skills, 3)
            skill1 = skill_3[0]
            skill2 = skill_3[1]
            skill3 = skill_3[2]
            context = {
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "job": fake.job(),
                    "town": fake.city(),
                    "strength": random.randint(3, 18),
                    "agility": random.randint(3, 18),
                    "endurance": random.randint(3, 18),
                    "intelligence": random.randint(3, 18),
                    "luck": random.randint(3, 18),
                    "skill_1": skill1,
                    "skill_2": skill2,
                    "skill_3": skill3
                    }
            n=n+1
            file_operations.render_template("charsheet.svg", "all_results/result{}.svg".format(n), context)
        exit()

if __name__ == '__main__':
    main()