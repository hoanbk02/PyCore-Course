# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

from datetime import datetime

""" Chương trình lấy các con số về dịch bệnh COVID,
    Dùng thư viện covid được cung cấp qua cài đặt: pip install covid
"""

from covid import Covid


covid = Covid()

# Toàn thế giới tính đến thời điểm chạy chương trình
print('In the World')
print('%25s' % 'Total confirmed cases:', '%10s' % covid.get_total_confirmed_cases())
print('%25s' % 'Total active cases:', '%10s' % covid.get_total_active_cases())
print('%25s' % 'Total recovered:', '%10s' % covid.get_total_recovered())
print('%25s' % 'Total deaths:', '%10s' % covid.get_total_deaths())

# print(covid.list_countries())

# Tính đến thời điểm chạy chương trình của một quốc gia cụ thể
list_countries = {
        0: 'Stop',
        1: 'Afghanistan',
        37: 'China',
        11: 'Italy',
        14: 'Russia',
        17: 'United Kingdom',
        18: 'US',
        25: 'Japan',
        27: 'India',
        108: 'Laos',
        183: 'Uzbekistan',
    }
while True:
    print('\n_____ ***** _____ _____ ***** _____ _____ ***** _____')
    print('Danh sách các quốc gia')
    print('%5s' % 'ID', 'Name')
    for id in list_countries:
        if id != 0:
            print('%5d' % id, list_countries.get(id))

    try:
        id_country = int(input('Nhập ID quốc gia bạn muốn truy vấn theo DS trên hoặc 0 nếu muốn kết thúc: '))
        while id_country not in list_countries:
            id_country = int(input('ID quốc gia nhập không đúng, xin vui lòng nhập lại:'))
    except:
        print('Bạn đã nhập không đúng :(')
        id_country = 0

    print('%s ==>> %s' % (id_country, list_countries[id_country]))
    if id_country == 0:
        break
    else:
        country_data = covid.get_status_by_country_id(id_country)
        country = country_data['country']
        confirmed = country_data['confirmed']
        active = country_data['active']
        deaths = country_data['deaths']
        recovered = country_data['recovered']
        latitude = country_data['latitude']
        longitude = country_data['longitude']
        last_update = datetime.fromtimestamp(country_data['last_update']/1000)
        print('_____ ***** _____ _____ ***** _____')
        print('Cập nhật vào lúc:', last_update, 'Quốc gia:', country, '(vĩ độ %s, kinh độ %s):' % (latitude, longitude))
        print('%12s' % 'Tổng số ca:', '%10s' % confirmed)
        print('%12s' % 'Tử vong:', '%10s' % deaths)
        print('%12s' % 'Phục hồi:', '%10s' % recovered)
        print('%12s' % 'Vẫn còn:', '%10s' % active)
        print('_____ ***** _____ _____ ***** _____')

    kt = input('Nhập 0 nếu muốn kết thúc HOẶC "enter" để tiếp tục: ')
    if kt == '0':
        print('%s ==>> Stop' % kt)
        break
    else:
        print('%s ==>> Continue' % kt)
        continue
