import re
from pprint import pprint
import csv
with open("phonebook.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

pattern = r'(\w+)\W*(\w+)\W*(\w+)\W*ФНС'
result = re.sub(pattern, r'\1,\2,\3, ФНС', contacts_list)
pattern_2 = r'(\w+)\W*(\w+)\W*(\w+)\W*Минфин'
result_2 = re.sub(pattern, r'\1,\2,\3, Минфин', contacts_list)

number_pattern = r'(\+7|8)\s?[(]?(\d{3})[)]?\s?-?(\d{3})-?(\d{2})-?(\d{2})'
number_result = re.sub(number_pattern, r'+7(\2)\3-\4-\5', contacts_list)
add_number_pattern = r'\+7\s?[(]?(\d{3})[)]?\s?-?(\d{3})-?(\d{2})-?(\d{2})\s?[(]?доб\.\s?(\d{4})[)]?'
add_number_result = re.sub(add_number_pattern, r'+7(\1)\2-\3-\4 доб.\5', contacts_list)

mail_pattern = r'[A-Z.a-z]+@[A-Z.a-z]+'
new_list =[]

# "([а-яА-Я, –]*)((\+7|8)\s?[(]?\d{3}[)]?\s?-?\d{3}-?\d{2}-?\d{2})?,?([A-Z.a-z0-9]+@[a-z]+\.ru)?"

with open("phonebook_new.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_list)


