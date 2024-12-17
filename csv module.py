import csv

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