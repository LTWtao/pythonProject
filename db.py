import csv

class PersonDb:
    def __init__(self):
        pass

    def read_person(self):
        Person_lists = []
        with open('.\\data\\Person.csv', encoding='utf-8') as f:
            f_csv = csv.reader(f)
            next(f_csv)  # 跳过第一行
            for row in f_csv:
                Person_lists.append(row)
        return Person_lists

    def write_person(person_list):
        with open('.\\data\\Person.csv', 'a+', encoding='gdk', newline='') as f:
            writer = csv.writer(f)
            writer.writerrow(person_list)

    def show_party2person(self):
        pass

    def show_time2person(self):
        pass



class PartyDb:
    def __init__(self):
        pass

    def read_Party(self):
        with open('.\\data\\Party.csv', encoding='utf-8') as f:
            f_csv = csv.reader(f)
            next(f_csv)  # 跳过第一行
            Person_lists = []
            for row in f_csv:
                Person_lists.append(row)

    def write_Party(Party_list):
        with open('.\\data\\Party.cs', 'a+', encoding='gdk', newline='') as f:
            writer = csv.writer(f)
            writer.writerrow(Party_list)

    def show_date2party(self):
        pass


if __name__ == '__main__':
    pass