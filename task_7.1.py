from pprint import pprint

cookbook = {}
list = ['ingredient_name', 'quantity', 'measure']
with open('recipes.txt', encoding='UTF-8') as file:
    for line in file:
        name = line.strip()
        ingredient_count = int(file.readline().strip())
        list2 = []
        for i in range(ingredient_count):
            line = file.readline().strip().split(' | ')
            couples = dict(zip(list, line))
            list2.append(couples)
        file.readline()
        cookbook[name] = list2
pprint(cookbook)

dishes = ['Омлет', 'Утка по-пекински', 'Запеченный картофель', 'Фахитос']
def get_shop_list_by_dishes(dishes, person_count):
    new_dict = {}
    for i in dishes:
        for j in cookbook[i]:
            if j['ingredient_name'] in new_dict:
                new_dict[j['ingredient_name']]['quantity'] += int(j['quantity']) * person_count
            else:
                new_dict[j['ingredient_name']] = {
                    'measure': j['measure'],
                    'quantity': int(j['quantity']) * person_count
            }
    pprint(new_dict)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)


