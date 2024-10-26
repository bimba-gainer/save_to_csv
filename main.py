import csv
import os

# Пути к файлам
input_file = 'addresses.txt'  # Файл с адресами Solana
output_dir = 'output_files/'  # Директория для сохранения CSV файлов

# Число адресов в каждом выходном файле
batch_size = 95

# Определяем заголовки вручную для сохранения порядка и структуры
headers = ["remark", "coin", "network", "address", "memo"]

# Читаем адреса из файла addresses.txt
def read_addresses(input_path):
    with open(input_path, 'r') as file:
        addresses = [line.strip() for line in file if line.strip()]
    return addresses

# Создание директории, если она не существует
def create_output_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

# Создание CSV файлов с последовательной нумерацией
def create_csv_files(addresses, headers, batch_size, output_dir):
    global_index = 1  # Глобальный счётчик для remark и диапазона файлов
    for i in range(0, len(addresses), batch_size):
        batch = addresses[i:i+batch_size]
        start_idx = global_index
        end_idx = start_idx + len(batch) - 1
        output_file = f'{output_dir}addresses_{start_idx}-{end_idx}.csv'
        
        # Записываем данные в CSV файл
        with open(output_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()  # Записываем заголовки
            for address in batch:
                writer.writerow({
                    "remark": global_index,
                    "coin": "SOL",
                    "network": "SOL",
                    "address": address,
                    "memo": ""
                })
                global_index += 1  # Увеличиваем глобальный индекс

# Главная функция
def main():
    create_output_dir(output_dir)  # Создаём выходную директорию
    addresses = read_addresses(input_file)  # Загружаем адреса
    create_csv_files(addresses, headers, batch_size, output_dir)

if __name__ == '__main__':
    main()

