import json


class JsonList:

    def __init__(self, name):
        self.name = name
        self.data = ""

    def save(self):
        with open(self.name, 'w', encoding="UTF-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2)

    def read(self):
        with open(self.name, 'r', encoding="UTF-8") as file:
            text = file.read()
        self.data = json.loads(text)

    def addData(self):
        title = input("Podaj tytul: \n")
        genre = input("Podaj gatunek: \n")
        rating = input("Podaj ocene: \n")

        self.data[title] = {'genre': genre,
                            'rating': rating}
        return self.data

    def deleteData(self):
        title = input("Podaj tytul do usuniecia: \n")
        del self.data[title]

    def showData(self):
        json_string = json.dumps(self.data, ensure_ascii=False, indent=2).encode("UTF-8")
        print(json_string.decode())

    def start(self):
        self.read()
        self.showData()
        while True:
            while True:
                x = input("Chcesz dodac nowy rekord? Y/N\n")
                if (x == 'Y') or (x == 'y'):
                    self.addData()
                elif (x == 'N') or (x == 'n'):
                    break
                else:
                    print("Podales zly znak, sprobuj ponownie\n")
            while True:
                x = input("Chcesz usunac rekord? Y/N\n")
                if (x == 'Y') or (x == 'y'):
                    self.deleteData()
                elif (x == 'N') or (x == 'n'):
                    break
                else:
                    print("Podales zly znak, sprobuj ponownie\n")
            while True:
                x = input("Chcesz zakonczyc prace? Y/N\n")
                if (x == 'Y') or (x == 'y'):
                    end = True
                    break
                elif (x == 'N') or (x == 'n'):
                    break
                else:
                    print("Podales zly znak, sprobuj ponownie\n")
            if end:
                break
        self.save()


if __name__ == '__main__':
    x = JsonList('filmy.json')
    x.start()
