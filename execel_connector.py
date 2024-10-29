import gspread


class ExcelConnector:
    def __init__(self):

        gc = gspread.service_account(filename='conf.json')

        table = gc.open_by_url(
            'https://docs.google.com/spreadsheets/d/1XGTMsbrI2T5p_xhmEV3afAFno3u1y9k7kWqUuzuOkrA/edit?gid=0#gid=0')

        self.worksheet = table.worksheet("teachers")

    def all_teachers(self):
        try:
            all_teachers = self.worksheet.get_all_values()[1:]
            for i in range(len(all_teachers)):
                all_teachers[i][6] = int(all_teachers[i][6])
                all_teachers[i][8] = int(all_teachers[i][8])
            return all_teachers
        except Exception as e:
            print(e)
            return False

    def search_by_subject(self, subject, teachers):
        return [i for i in teachers if i[3].lower() == subject.lower()]

    def search_by_name(self, name, teachers):
        return [i for i in teachers if i[1].lower() == name.lower()]

    def search_by_surname(self, surname, teachers):
        return [i for i in teachers if i[2].lower() == surname.lower()]

    def search_by_class(self, class_num: int, teachers):
        result = []
        for teacher in teachers:
            down, high = teacher[4].split('-')
            if int(down) <= class_num <= int(high):
                result.append(teacher)
        return result

    def search_by_place(self, place, teachers):
        return [i for i in teachers if len(set(i[5]) & set(place)) >= 3]

    def search_by_tariff(self, tariff, teachers):
        return [i for i in teachers if int(i[6]) <= tariff]

    def search_by_achievements(self, achievement, teachers):
        return [i for i in teachers if len(set(i[7]) & set(achievement)) >= 3]

    def teacher_by_id(self, id):
        try:
            teacher = [i for i in self.worksheet.get_all_values()[1:] if int(i[0]) == id][0]
            teacher[0] = int(teacher[0])
            teacher[6] = int(teacher[6])
            teacher[8] = int(teacher[8])
            return teacher
        except Exception as e:
            print(e)
            return False





if __name__ == '__main__':
    connector = ExcelConnector()
    all_teachers = connector.all_teachers()
    print(all_teachers)
    print(connector.search_by_tariff(10000, teachers=all_teachers))