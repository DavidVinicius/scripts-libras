# -*- coding: utf-8 -*-
import csv
rows = []
with open('test.csv', "rb") as file:
    content = file.readlines()
header = content[:1]
rows = content[1:2]
print(header)
print(rows)