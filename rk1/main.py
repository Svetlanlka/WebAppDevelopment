# Предметная область 9: 
# Операционная система - компьютер
# Запросы Д:
#   1.«Операционная система» и «Компьютер» связаны соотношением один-ко-многим.
#     Выведите список всех операционных систем, у которых название хранимой записи содержит "Windows", и названия компьютеров с этими ОС.
#   2.«Операционная система» и «Компьютер» связаны соотношением один-ко-многим.
#     Выведите список компьютеров со средней датой публикации операционных систем в каждом компьютере, отсортированный по средней дате публикации.
#     (отдельной функции вычисления среднего значения в Python нет, нужно использовать комбинацию функций вычисления суммы и количества значений).
#   3. «Операционная система» и «Компьютер» связаны соотношением многие-ко-многим.
#     Выведите список всех компьютеров, у которых название начинается с буквы «А», и список их операционных систем.

from operator import itemgetter
from store.computer import computers
from store.operating_system import operating_systems
from store.operating_system_computer import computers_with_operation_systems

def main():
  # Соединение данных один-ко-многим 
  operating_systems_join_computers = [{'operating_systems': o, 'computers': c}
    for o in operating_systems
    for c in computers 
    if o.computer_id == c.id
  ]

  print('Задание Д-1')
  # Выведем id, name, publication_year таблицы "Операционная система"
  # При этом name != Windows
  # И выведем компьютеры этих ОС
  D1 = [(x['operating_systems'].id, x['operating_systems'].name, x['operating_systems'].publication_year, x['computers'].name)
    for x in operating_systems_join_computers
    if x['operating_systems'].name.find('Windows') != - 1
  ]
  for x in D1:
    print(x)
  

  print('\nЗадание Д-2')
  # Выведем имя компьютера, среднее по дате публикации ОС этого компьютера
  # Сортируя по этому среднему

  # Заведем таблицу с накапливаемой суммой дат и кол-вом ОС:
  computer_sum_count_dict = {}
  for os_computers_row in operating_systems_join_computers:
    computer_name = os_computers_row['computers'].name
    publication_year = os_computers_row['operating_systems'].publication_year

    if computer_name in computer_sum_count_dict:
      computer_sum_count_dict[computer_name]['sum'] = computer_sum_count_dict[computer_name]['sum'] + publication_year
      computer_sum_count_dict[computer_name]['count'] = computer_sum_count_dict[computer_name]['count'] + 1
    else:
      computer_sum_count_dict[computer_name] = {'sum': publication_year, 'count': 1}

  D2 = sorted(
    [(computer_name, computer_sum_count_dict[computer_name]['sum'] / computer_sum_count_dict[computer_name]['count'])
      for computer_name in computer_sum_count_dict
      if computer_sum_count_dict[computer_name]['count'] != 0
    ],
    key=itemgetter(1), reverse=True
  )
  for x in D2:
    print(x)

  print('\nЗадание Д-3')

  # Соединение данных многие-ко-многим
  many_to_many = [(c.name, co.computer_id, co.operation_system_id)
    for c in computers
        for co in computers_with_operation_systems 
            if c.id == co.computer_id]

  computers_with_operation_systems_table = [(operating_system.name, operating_system.publication_year, computer_name)
    for computer_name, computer_id, operating_system_id in many_to_many
        for operating_system in operating_systems if operating_system.id == operating_system_id]

  D3 = {}
  for computer in computers:
    if computer.name.startswith('A'):
        operating_systems_of_computer = list(filter(lambda i: i[2] == computer.name, computers_with_operation_systems_table))
        operating_systems_names = [x for x, _, _ in operating_systems_of_computer]
        D3[computer.name] = operating_systems_names

  print(D3)
 
if __name__ == '__main__':
  main()
