"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        table = soup.find('tbody')
        total_male_number = 0
        total_female_number = 0
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:  # 確保有排名、名字和人數（至少有5個欄位）
                male_number = int(cols[2].text.replace(',', ''))
                female_number = int(cols[4].text.replace(',', ''))
                total_male_number += male_number
                total_female_number += female_number
        print(f"Male Number: {total_male_number}")
        print(f"Female Number: {total_female_number}")


if __name__ == '__main__':
    main()
