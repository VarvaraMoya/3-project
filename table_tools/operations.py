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