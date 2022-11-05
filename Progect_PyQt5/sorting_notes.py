class SortingNormal:
    @staticmethod
    def sort():
        file = open('files/name_files.txt', 'rt')
        names_files = file.readlines()
        names_files_datetime = {}
        file.close()
        for i in names_files:
            file = open(f'files/{i[:-1]}/editing_time.txt', mode='rt')
            names_files_datetime[i] = file.readline()
            file.close()
        names_files_datetime = sorted(names_files_datetime, key=names_files_datetime.get)
        file = open('files/name_files.txt', mode='w')
        file.close()
        file = open('files/name_files.txt', mode='a')
        for i in names_files_datetime[::-1]:
            file.write(i)
        file.close()


class SortingName:
    @staticmethod
    def sort():
        file = open('files/name_files.txt', 'rt')
        names_files = file.readlines()
        file.close()
        list_title = {}
        for i in names_files:
            name = i[:-1]
            file = open(f'files/{name}/title.txt')
            title = file.readline()
            file.close()
            list_title[name] = title
        list_title = sorted(list_title, key=list_title.get)
        file = open('files/name_files.txt', mode='w')
        file.close()
        file = open('files/name_files.txt', mode='a')
        for i in list_title:
            file.write(f'{i}\n')
        file.close()

