from bs4 import BeautifulSoup
import requests

job_boards = ['https://devkg.com/ru/jobs', 'https://bishkek.headhunter.kg/']
keywords = ['junior', 'python', 'backend']

# if __name__ == 'main':
main_page = requests.get(job_boards[0]).text
soup = BeautifulSoup(main_page, 'lxml')
divs = soup.find('div', class_='page').find('div', class_='jobs-list').find_all('div', class_='jobs-item')
# divs = soup.find('div', class_='data-v-955d805c') data-v-3fc4231a

print(main_page)
# div containing pagination class: 'pagination', the link's class: 'nav nuxt-link-active'

print(len(divs))
for div in divs:
    position = div.find('div', class_='jobs-item-field position').text
    position = position.replace('Должность', '').strip()
    print(position, "\n------------------------")
