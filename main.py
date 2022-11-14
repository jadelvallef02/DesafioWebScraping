import bs4
import requests

url = 'https://www.filmaffinity.com/es/ranking.php?rn=ranking_scifi'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
movies = soup.select('.movie-card .mc-poster a')
for m in movies:
    print(m.attrs['href'])
