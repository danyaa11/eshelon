import requests
import lxml.html
import cssselect
from selenium import webdriver
import time
from test_data.data import user_name, email, password, repo_name, file_name, file_text, url
from selenium.webdriver.common.by import By
from test_data import locators as loc
import os


driver = webdriver.Chrome("C:\\Users\\danya\\PycharmProjects\\http 15.05\\chromedriver")
driver.implicitly_wait(2)

def open_page():
    driver.maximize_window()
    driver.get(url)

def registrate_user():
    registration_elem = driver.find_element(By.CSS_SELECTOR, loc.registration_elem_css)
    registration_elem.click()
    user_name_input_el = driver.find_element(By.CSS_SELECTOR, loc.user_name_input_el_css)
    user_name_input_el.send_keys(user_name)
    email_input_el = driver.find_element(By.CSS_SELECTOR, loc.email_input_el_css)
    email_input_el.send_keys(email)
    password_input_el = driver.find_element(By.CSS_SELECTOR, loc.password_input_el_css)
    password_input_el.send_keys(password)
    retype_passwd_input_el = driver.find_element(By.CSS_SELECTOR, loc.retype_passwd_input_el_css)
    retype_passwd_input_el.send_keys(password)
    button_registr_confirm = driver.find_element(By.CSS_SELECTOR, loc.button_registr_confirm_css)
    button_registr_confirm.click()

def create_repo():
    repo_create_el = driver.find_element(By.CSS_SELECTOR, loc.repo_create_el_css)
    repo_create_el.click()
    input_repo_name_el = driver.find_element(By.CSS_SELECTOR, loc.input_repo_name_el_css)
    input_repo_name_el.send_keys(repo_name)
    add_readme_checkbox = driver.find_element(By.XPATH, loc.add_readme_checkbox_xpath)
    add_readme_checkbox.click()
    create_repo_button = driver.find_element(By.CSS_SELECTOR, loc.create_repo_button_css)
    create_repo_button.click()

def add_commit_file():
    add_file_menu = driver.find_element(By.XPATH, loc.add_file_menu_xpath)
    add_file_menu.click()
    new_file_button = driver.find_element(By.XPATH, loc.new_file_button_xpath)
    new_file_button.click()
    file_name_input = driver.find_element(By.CSS_SELECTOR, loc.file_name_input_css)
    file_name_input.send_keys(file_name)
    text_input = driver.find_element(By.XPATH, loc.text_input_xpath)
    text_input.send_keys(file_text)
    commit_button = driver.find_element(By.CSS_SELECTOR, loc.commit_button_css)
    commit_button.click()

def show_text_in_file():
    to_main_page_repo = driver.find_element(By.XPATH, loc.to_main_page_repo_xpath)
    to_main_page_repo.click()
    file_href = driver.find_element(By.XPATH, loc.file_href_xpath)
    file_href.click()
    file_view = driver.find_element(By.XPATH, loc.file_view_xpath)
    text = file_view.text
    return text









