import pickle

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