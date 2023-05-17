import time
import pytest
import requests
import lxml.html
from test_data import data
from test_data.data import url, file_text, port
from test_data import locators as loc
import actions
import os


os.chdir("C://Users//danya//PycharmProjects//http 15.05")
os.system("docker-compose up -d")
time.sleep(4)
responce = requests.get(url)
html_tree = lxml.html.fromstring(responce.text)
actions.open_page()

def test_connecting_to_url():
    assert responce.status_code == 200, f'host isn\'t available on port {port}'

def test_existing_el1():
    flame_el = html_tree.cssselect(loc.etalon_css_el_flame)
    desktop_el = html_tree.cssselect(loc.etalon_css_el_desktop)
    rocket_el = html_tree.cssselect(loc.etalon_css_el_rocket)
    assert len(flame_el) != 0, "Flame element not found"
    assert len(desktop_el) != 0, "Desktop element not found"
    assert len(rocket_el) != 0, "Rocket element not found"

def test_existing_etalon_text():
    text_el = html_tree.cssselect(loc.etalon_css_main_text)[0]
    text = text_el.text_content().strip()
    assert text == data.etalon_text, "Etalon text not found"

actions.registrate_user()
actions.create_repo()
actions.add_commit_file()

def test_equality_file_text():
    assert actions.show_text_in_file() == file_text, "text in file isn't equal to input text"
















