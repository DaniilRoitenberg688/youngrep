import sqlite3
from sqlite3 import connect

from flask import Flask


class BdConnector:
    def __init__(self, bd_name):
        self.name = bd_name

    def all_teachers(self):
        try:
            connection = sqlite3.connect(self.name)
            cursor = connection.cursor()
            all_teachers = cursor.execute('SELECT * FROM teachers').fetchall()
            return all_teachers
        except Exception as e:
            print(e)
            return False

    def search_by_subject(self, subject, teachers):
        return [i for i in teachers if i[2].lower() == subject.lower()]

    def search_by_name(self, name, teachers):
        return [i for i in teachers if i[0].lower() == name.lower()]

    def search_by_surname(self, surname, teachers):
        return [i for i in teachers if i[1].lower() == surname.lower()]

    def search_by_class(self, class_num: int, teachers):
        result = []
        for teacher in teachers:
            down, high = teacher[3].split('-')
            if int(down) <= class_num <= int(high):
                result.append(teacher)
        return result

    def search_by_place(self, place, teachers):
        return [i for i in teachers if len(set(i[4]) & set(place)) >= 3]

    def search_by_tariff(self, tariff, teachers):
        return [i for i in teachers if i[5] <= tariff]

    def search_by_achievements(self, achievement, teachers):
        return [i for i in teachers if len(set(i[6]) & set(achievement)) >= 3]




if __name__ == '__main__':
    connector = BdConnector('rep.db')
    all_teachers = connector.all_teachers()
    print(all_teachers)
    print(connector.search_by_tariff(10000, teachers=all_teachers))