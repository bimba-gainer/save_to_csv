# Solana Addresses CSV Formatter for COINEX White Lists

Этот проект на Python предназначен для форматирования списка Solana адресов, сохранённых в текстовом файле `addresses.txt`, и их распределения в файлы CSV по шаблону для загрузки в белые списки биржи COINEX. 
Программа создаёт CSV файлы с заданной структурой и разделением на батчи по 95 адресов, а также сохраняет последовательную нумерацию как в столбце `remark`, так и в названии файлов.

## Структура проекта

- `main.py` — основной скрипт для выполнения форматирования и распределения адресов по CSV файлам.
- `addresses.txt` — текстовый файл со списком Solana адресов (по одному адресу на строку).
- `output_files/` — директория, куда сохраняются выходные CSV файлы.

## Установка и использование

1. Клонируйте репозиторий и перейдите в папку проекта:

    ```bash
    git clone <URL-репозитория>
    cd <папка-проекта>
    ```

2. Убедитесь, что Python 3 установлен в вашей системе. Если нет, установите его с [официального сайта Python](https://www.python.org/downloads/).

3. Убедитесь, что файл `addresses.txt` находится в той же директории, что и `main.py`.

4. Запустите скрипт:

    ```bash
    python main.py
    ```

## Детали работы скрипта

### Входные файлы

- **`addresses.txt`**: Этот файл должен содержать один Solana адрес на каждой строке.

### Выходные файлы

- Скрипт создаёт несколько CSV файлов в папке `output_files`. Каждый файл будет содержать максимум 95 адресов.
- Каждый CSV файл содержит следующие столбцы: `remark`, `coin`, `network`, `address`, и `memo`.
- Нумерация `remark` и название файла идут последовательно, без сброса на каждом новом файле.

### Пример выходного файла

Имя файла: `addresses_1-95.csv`

Содержание:

```csv
remark,coin,network,address,memo
1,SOL,SOL,8tJPfER1mgc4kvbVDi3eEQ3EskYxHmTn1bwm8DLAfapb,
2,SOL,SOL,6mXp7HLUQT1BKWcDx6tzkMFvco5Zy1C6AszK8CUsYR5p,
3,SOL,SOL,CLYAY4ZGnz4j13zvrQAJAYpUnb5VMsFqsWdXPosczmRt,
...
