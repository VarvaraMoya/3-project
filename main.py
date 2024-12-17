import csv
import pickle

class Table:
    def __init__(self, data=None):
        self.data = data or []
        self.column_types = {}

    def load_csv(self, filename):
        """Загрузка таблицы из CSV файла."""
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                self.data = [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f'Файл {filename} не найден.')
        except Exception as e:
            raise Exception(f'Ошибка при загрузке CSV: {e}')

    def save_csv(self, filename):
        """Сохранение таблицы в CSV файл."""
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(self.data)
        except Exception as e:
            raise Exception(f'Ошибка при сохранении в CSV: {e}')

    def load_pickle(self, filename):
        """Загрузка таблицы из Pickle файла."""
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f'Файл {filename} не найден.')
        except Exception as e:
            raise Exception(f'Ошибка при загрузке Pickle: {e}')

    def save_pickle(self, filename):
        """Сохранение таблицы в Pickle файл."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.data, file)
        except Exception as e:
            raise Exception(f'Ошибка при сохранении в Pickle: {e}')

    def save_text(self, filename):
        """Сохранение таблицы в текстовый файл."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for row in self.data:
                    file.write('\t'.join(map(str, row)) + '\n')
        except Exception as e:
            raise Exception(f'Ошибка при сохранении в текстовый файл: {e}')

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        """Получение строк по номерам."""
        stop = stop or start
        rows = self.data[start:stop + 1]
        if copy_table:
            return Table(rows)
        return rows

    def get_rows_by_index(self, *vals, copy_table=False):
        """Получение строк по значениям в первом столбце."""
        rows = [row for row in self.data if row[0] in vals]
        if copy_table:
            return Table(rows)
        return rows

    def get_column_types(self, by_number=True):
        """Получение типов данных в столбцах."""
        if by_number:
            return {i: self.column_types.get(i, str) for i in range(len(self.data[0]))}
        else:
            return self.column_types

    def set_column_types(self, types_dict, by_number=True):
        """Задание типов данных для столбцов."""
        if by_number:
            self.column_types = {i: types_dict.get(i, str) for i in range(len(self.data[0]))}
        else:
            self.column_types = types_dict

    def get_values(self, column=0):
        """Получение значений столбца."""
        try:
            return [self._convert_value(row[column], column) for row in self.data]
        except IndexError:
            raise IndexError(f'Столбец с индексом {column} не найден.')

    def get_value(self, column=0):
        """Получение значения из одного столбца для одной строки."""
        try:
            return self._convert_value(self.data[0][column], column)
        except IndexError:
            raise IndexError(f'Столбец с индексом {column} не найден.')

    def set_values(self, values, column=0):
        """Задание значений столбца."""
        try:
            for i, value in enumerate(values):
                self.data[i][column] = self._convert_value(value, column)
        except IndexError:
            raise IndexError(f'Столбец с индексом {column} не найден.')

    def set_value(self, value, column=0):
        """Задание одного значения столбца для одной строки."""
        try:
            self.data[0][column] = self._convert_value(value, column)
        except IndexError:
            raise IndexError(f'Столбец с индексом {column} не найден.')

    def _convert_value(self, value, column):
        """Конвертация значений в нужный тип."""
        column_type = self.column_types.get(column, str)
        if column_type == int:
            return int(value)
        elif column_type == float:
            return float(value)
        elif column_type == bool:
            return bool(value)
        return str(value)

    def print_table(self):
        """Вывод таблицы."""
        if not self.data:
            print("Таблица пуста.")
        else:
            for row in self.data:
                print('\t'.join(map(str, row)))


# Пример использования:
Table = Table([["ID", "Name", "Age"], [1, "Alice", 30], [2, "Bob", 25], [3, "Charlie", 35]])

# Вывод таблицы
Table.print_table()
