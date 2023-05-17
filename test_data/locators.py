from test_data.data import file_name

registration_elem_css = "[href *= 'sign_up']"
user_name_input_el_css = "#user_name"
email_input_el_css = "#email"
password_input_el_css = "#password"
retype_passwd_input_el_css = "#retype"
button_registr_confirm_css = "button[class='ui green button']"
repo_create_el_css = ".tooltip[href*='repo/create']"
input_repo_name_el_css = "#repo_name"
add_readme_checkbox_xpath = "//label[contains(text(),'README') and contains(text(),'LICENSE')]"
create_repo_button_css = "[class = 'ui green button']"
add_file_menu_xpath = "//button[1][@role='menu']"
new_file_button_xpath = "//button[1][@role='menu']//a[contains(@href, 'new')]"
file_name_input_css = "#file-name"
text_input_xpath = "//textarea[contains(@class,'input')]"
commit_button_css = "#commit-button"
to_main_page_repo_xpath = "//a[@class = 'section']"
file_href_xpath = "//a[contains(@title, '" + file_name + "')]"
file_view_xpath = "//code"

etalon_css_el_flame = "[class='svg octicon-flame']"
etalon_css_el_desktop = "[class='svg octicon-device-desktop']"
etalon_css_el_rocket = "[class='svg octicon-rocket']"
etalon_css_main_text = "[class='ui icon header title']"