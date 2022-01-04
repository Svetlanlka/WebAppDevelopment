import sqlite3
from django.core.management.base import BaseCommand

donuts_values = [
  ('Пончик "Звездное Небо', 'Вам нравиться наблюдать за красотой ночного неба? За звездами, раскиданными \
по нему. Тогда вам обязательно стоит попробовать наше изделие.', 110, 'donut-1.jpg'),
  ('Пончик "Космическая радость"', 'Этот пончик космически красив и обязательно порадует вас своим вкусом. ', 120, 'donut-2.jpg'),
  ('Пончик "Галактика"', 'Вкус этого пончика превосходен. Говорят, что его создатели обладали \
знаниями, присланными издалека, с конца нашей галактики.', 95, 'donut-3.jpg'),
  ('Ринг Новогодний', 'Обязательно попробуйте наше новогоднее чудо', 105, 'donut-4.png'),
  ('Пончик Дед Мороз', 'Этот дед мороз уже спешит к вам в новогоднюю ночь с подарками', 150, 'donut-5.jpg'),
  ('Пончик Ёлка', 'Как же в новогодний вечер без елочки ? Обязательно добавьте этот пончик к себе на стол, \
и новогоднее настроение вам обеспечено', 90, 'donut-6.jpg'),
  ('Пончик Шоколадка', 'С шоколадной начинкой, шоколадной глазурью и шоколадной крошкой.', 130, 'donut-7.png'),
  ('Пончик Сердце', 'С клубничной начинкой, серой сахарной глазурью и посыпкой "шарики"', 135, 'donut-8.png'),
  ('Ореховый пончик', 'С ореховой посыпкой и сгущенкой в качестве начинки', 120, 'donut-9.jpg'),
  ('Черри Перри', 'С вишнёвой начинкой и вишнёвой шоколадной глазурью.', 155, 'donut-10.png'),
  ('Фисташковая мечта', 'С фисташковым кремом, сахарной глазурью и лепестками арахиса.', 190, 'donut-11.png'),
  ('Голубой Питер', 'С джемовой малиновой начинкой, голубой ванильной глазурью и маршмеллоу.', 115, 'donut-12.png'),
]

sets_values = [
  ('Стандартный сет', 'Здесь собраны пончики на любой вкус. Вам обязательно понравится!', 'set-3.jpeg'),
  ('Сет "Космос"', 'Наш фирменный набор пончиков с тематикой космоса', 'set-1.jpg'),
  ('Новогодний сет', 'Компания наших пончиков позволит Вам встретить Новый Год с улыбкой', 'set-2.jpg'),
]

fk_values = [
  ('1', '7'),
  ('1', '8'),
  ('1', '9'),
  ('1', '10'),
  ('1', '11'),
  ('1', '12'),
  ('2', '1'),
  ('2', '2'),
  ('2', '3'),
  ('3', '4'),
  ('3', '5'),
  ('3', '6'),
]

fill_sets_query = "INSERT INTO donutssets (name, info, picture) VALUES (?, ?, ?);"
fill_donuts_query = "INSERT INTO donuts (name, info, cost, picture) VALUES (?, ?, ?, ?);"
fill_donutssets_fk_donuts_query = "INSERT INTO donutssets_fk_donuts (donutsset_id, donut_id) VALUES (?, ?);"

class Command(BaseCommand):
  help = "filling db donuts"

  def handle(self, *args, **options):
    self.fillDonuts()
    self.fillDonutsSets()
    self.fillDonutsFkSets()

  def fillDonuts(self):
    db = sqlite3.connect("donuts.sqlite3")
    c=db.cursor()

    for donut in donuts_values:
      c.execute(fill_donuts_query, donut)

    db.commit()
    c.close()
    db.close()

  def fillDonutsSets(self):
    db = sqlite3.connect("donuts.sqlite3")
    c=db.cursor()

    for set in sets_values:
      c.execute(fill_sets_query, set)

    db.commit()
    c.close()
    db.close()

  def fillDonutsFkSets(self):
    db = sqlite3.connect("donuts.sqlite3")
    c=db.cursor()

    for fk in fk_values:
      c.execute(fill_donutssets_fk_donuts_query, fk)

    db.commit()
    c.close()
    db.close()