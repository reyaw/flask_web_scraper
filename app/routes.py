from flask.helpers import url_for
from app.models import Player
from flask import current_app as app, redirect
from flask.json import jsonify
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
import requests

@app.route('/')
def scrape():
    def get_player_data(player_name):
        print("Begin web scraping...")

        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        driver.get('https://www.nbastuffer.com/')

        link_to_click = driver.find_elements_by_class_name('x-recent-post6')[3]
    #     link_to_click = driver.find_element_by_xpath("//a[@title='Permalink To: \'2020-2021 NBA Player Stats\']")
        link_to_click.click()


        option_to_select = driver.find_elements_by_class_name('x-nav-tabs-item')[0]
        option_to_select.click()


        search_field = driver.find_element_by_tag_name('input')
        search_term = player_name
        search_field.send_keys(player_name)


        page = requests.get(driver.current_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        tbody = soup.find('tbody', class_='row-hover')

        player_list = [tr for idx, tr in enumerate(list(tbody.children)) if idx % 2 != 0]
        for idx, td in enumerate(player_list):
            stats_list = list(td.children)[1:-2]
            player_name = stats_list[1].text
            if player_name == search_term:
                print(player_name)
                break

        s = stats_list
        p = Player(
            name=s[1].text,
            team=s[2].text,
            position=s[3].text,
            age=float(s[4].text),
            games_played=int(s[5].text),
            minutes_per_game=float(s[6].text),
            ft_attempts=int(s[10].text),
            ft_percentage=float(s[11].text),
            tp_attempts=int(s[12].text),
            tp_percentage=float(s[13].text),
            th_attempts=int(s[14].text),
            th_percentage=float(s[15].text),
            points_per_game=float(s[18].text),
            rebounds_per_game=float(s[19].text),
            assists_per_game=float(s[21].text),
            steals_per_game=float(s[23].text),
            blocks_per_game=float(s[24].text),
            turnovers_per_game=float(s[25].text),
        )
        p.save()
        driver.close()
        print('Web scraping complete')

    get_player_data('Giannis Antetokounmpo')
    sleep(6)
    
    return redirect('/')
    
