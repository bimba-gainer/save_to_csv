import csv

# Пути к файлам
input_file = 'addresses.txt'    # Файл с адресами Solana
template_file = 'sample.csv'    # Файл-шаблон для структуры
output_dir = 'output_files/'    # Директория для сохранения CSV файлов

# Число адресов в каждом выходном файле
batch_size = 95

# Читаем шаблон из sample.csv для столбцов
def read_template_columns(template_path):
    with open(template_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
    return headers

# Читаем адреса из файла addresses.txt
def read_addresses(input_path):
    with open(input_path, 'r') as file:
        addresses = [line.strip() for line in file if line.strip()]
    return addresses

# Создание CSV файлов с заданным шаблоном
def create_csv_files(addresses, headers, batch_size, output_dir):
    for i in range(0, len(addresses), batch_size):
        batch = addresses[i:i+batch_size]
        start_idx = i + 1
        end_idx = start_idx + len(batch) - 1
        output_file = f'{output_dir}addresses_{start_idx}-{end_idx}.csv'
        
        # Записываем данные в CSV файл
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for j, address in enumerate(batch, start=1):
                writer.writerow([j, 'SOL', 'SOL', address, ''])

# Главная функция
def main():
    headers = read_template_columns(template_file)
    addresses = read_addresses(input_file)
    create_csv_files(addresses, headers, batch_size, output_dir)

if __name__ == '__main__':
    main()

