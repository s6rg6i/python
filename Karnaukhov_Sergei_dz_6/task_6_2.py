# 6.2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
# из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.


nginx_log = {}
# Определяем самых активных через словарь { ip : <количество> }
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        key = line.split('"', maxsplit=1)[0].split(maxsplit=1)[0]
        nginx_log[key] = 1 if nginx_log.get(key) is None else nginx_log[key] + 1
print(f'(Всего IP адресов: {len(nginx_log)}')
print('Определяем самых активных. 1-й способ: через словарь')
sorted_keys = sorted(nginx_log, key=nginx_log.get, reverse=True)
for i in range(10):
    qw = nginx_log[sorted_keys[i]]
    print(sorted_keys[i], qw)

print('Определяем самого активного. 2-й способ: через функцию max()')
ip_addrs = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        key = line.split('"', maxsplit=1)[0].split(maxsplit=1)[0]
        ip_addrs.append(key)
max_req = max(set(ip_addrs), key=ip_addrs.count)
max_qw = ip_addrs.count(max_req)
print(max_req, max_qw)
