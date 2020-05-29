from bs4 import BeautifulSoup
import requests

def convertToArrayDivTag(any):
    arr = []
    for item in any:
        res = item.find('div').get_text()
        arr.append(res)
    arr.remove(arr[0])
    return arr

def convertToArraySpanTag(any):
    arr = []
    td = any.find_all('span')
    for item in td:
        res = item.get_text()
        arr.append(res)
    return arr

def convertoArrayDays(any):
    arr =[]
    for item in any:
        td_name = item.find('span', 'b-forecast__table-days-name').get_text()
        td_date = item.find('span', 'b-forecast__table-days-date').get_text()
        val = td_name + ' - ' + td_date
        arr.append(val)
    return arr

def converToArrayTitle(any):
    t = any.find_all('td')
    arr = []
    for item in t:
         div = item.find('div').get_text()
         p = item.find('p').get_text()
         val = div + ' - ' + p
         arr.append(val)
    return arr

def res(city):
    headers = requests.utils.default_headers()
    url = 'https://www.weather-forecast.com/locations/{}/forecasts/latest'.format(city)
    req = requests.get(url, headers)
    bs = BeautifulSoup(req.content, 'html.parser')
    table = bs.find('table')
    tr = table.find_all('td', 'b-forecast__table-days-item')
    tr_daytimes = table.find('tr', 'b-forecast__table-time')
    tr_summary = table.find('tr', 'b-forecast__table-summary')
    tr_maxtemp = table.find('tr', 'b-forecast__table-max-temperature')
    tr_mintemp = table.find('tr', 'b-forecast__table-min-temperature')
    tr_title = table.find('tr', 'b-forecast__table-description')
    arr_summary = convertToArrayDivTag(tr_summary)
    arr_daytimes = convertToArrayDivTag(tr_daytimes)
    arr_maxtemp = convertToArraySpanTag(tr_maxtemp)
    arr_mintemp = convertToArraySpanTag(tr_mintemp)
    arr_days = convertoArrayDays(tr)
    arr_title = converToArrayTitle(tr_title)
    j = 1
    print("Located: ", city)
    print(arr_title[0])
    if len(arr_days) == 12:
     for i in arr_days:
        if j == 10:
            print(arr_title[1])
        if j == 19:
            print(arr_title[2])
        if j == 28:
            print(arr_title[3])
        print(arr_days[i])
        if (j < len(arr_daytimes)):
            print(arr_daytimes[0] + ": High/Low " + arr_maxtemp[j - 1] + "/" + arr_mintemp[j - 1] + ", detail: " +
                  arr_summary[j - 1])
            print(
                arr_daytimes[1] + ": High/Low " + arr_maxtemp[j] + "/" + arr_mintemp[j] + ", detail: " + arr_summary[j])
            print(arr_daytimes[2] + ": High/Low " + arr_maxtemp[j + 1] + "/" + arr_mintemp[j + 1] + ", detail: " +
                  arr_summary[j + 1])
        j += 3
        print('---------')
    else:
        print(arr_days[0])
        print(arr_daytimes[1] + ": High/Low " + arr_maxtemp[0] + "/" + arr_mintemp[0] + ", detail: " + arr_summary[0])
        print(arr_daytimes[2] + ": High/Low " + arr_maxtemp[1] + "/" + arr_mintemp[1] + ", detail: " + arr_summary[1])
        print('---------')
        for i in range(1, len(arr_days) - 2):
            if j == 10:
                print(arr_title[1])
            if j == 19:
                print(arr_title[2])
            if j == 28:
                print(arr_title[3])
            print(arr_days[i])
            if (j < len(arr_daytimes) -1):
                print(arr_daytimes[0] + ": High/Low " + arr_maxtemp[j - 1] + "/" + arr_mintemp[j - 1] + ", detail: " +
                      arr_summary[j - 1])
                print(
                    arr_daytimes[1] + ": High/Low " + arr_maxtemp[j] + "/" + arr_mintemp[j] + ", detail: " +
                    arr_summary[j])
                print(arr_daytimes[2] + ": High/Low " + arr_maxtemp[j + 1] + "/" + arr_mintemp[j + 1] + ", detail: " +
                      arr_summary[j + 1])
            j += 3
            print('---------')
        print(arr_days[len(arr_days) - 1])
        print(arr_daytimes[0] + ": High/Low " + arr_maxtemp[len(arr_maxtemp) - 1 ] + "/" + arr_mintemp[len(arr_mintemp) - 1] + ", detail: " + arr_summary[len(arr_summary) - 1])
if __name__ == '__main__':
    while True:
        print('////////////////////////////////////////////////////')
        city = input("Nhap ten thanh pho: ")
        res(city)



