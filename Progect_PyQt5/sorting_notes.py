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
        names_files = [int(i[:-1]) for i in names_files]
        file.close()
        file = open('files/name_files.txt', mode='w')
        file.close()
        file = open('files/name_files.txt', mode='a')
        for i in sorted(names_files):
            file.write(str(i) + '\n')
        file.close()
