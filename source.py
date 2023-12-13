import requests
import csv
 
def get_all_pages():
    base_url = 'http://54.37.12.181:1337/api/sneakers'
    page_size = 100
    current_page = 1
    all_pages = []
 
    try:
        while True:
            response = requests.get(base_url, params={
                'pagination[page]': current_page,
                'pagination[pageSize]': page_size
            })
 
            data = response.json()
            all_pages.extend(data['data'])
 
            if len(data['data']) < page_size:
                break
            current_page += 1
 
        with open('all_Sne.csv', 'w') as file:
            csv.dump(all_pages, file)
        print('All pages saved to Sne.csv')
    except Exception as error:
        print('Error:', str(error))
 
get_all_pages()
