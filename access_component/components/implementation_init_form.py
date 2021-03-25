from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InitForm:
    __url_access_system = "https://192.168.250.17:8005/"
    option = webdriver.ChromeOptions()

    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 2
    })

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.option)
        self.driver.get(self.__url_access_system)
        self.driver.maximize_window()

    def clear_input(self, path_input):
        self.driver.find_element_by_xpath(path_input).clear()


class InitFormWeb(InitForm):
    __xpath_window_initial = '//*[@id="requirements"]/div/div[1]/div/div/img'
    __xpath_button_init = "/html/body/app-root/app-digital-account/div/div[4]/button"
    __xpath_details = '//*[@id="details-button"]'
    __xpath_link_access = '//*[@id="proceed-link"]'
    __xpath_text_modal_init = '/html/body/alert-modal/div/div[1]/div/text-component[1]/div'
    __xpath_button_accept_modal = "/html/body/alert-modal/div/div[1]/div/div[2]/button"

    def view_windows_initial(self):
        try:
            windows_initial = WebDriverWait(self.driver, 20).\
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_window_initial)))
            return windows_initial.is_displayed()
        except Exception as inst:
            print("Error: The view windows initial", inst)

    def click_button_details(self):
        try:
            button_details = WebDriverWait(self.driver, 20).\
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_details)))
            return button_details.click()
        except Exception as inst:
            print("Error: By clicking on the button details", inst)

    def click_link_access(self):
        try:
            link_access = WebDriverWait(self.driver, 20).\
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_link_access)))
            return link_access.click()
        except Exception as inst:
            print("Error: By clicking on the link access", inst)

    def click_button_init(self):
        try:
            button_details = WebDriverWait(self.driver, 20).\
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_button_init)))
            return button_details.click()
        except Exception as inst:
            print("Error:By clicking on the button init", inst)

    def get_modal_coverage(self):
        try:
            text_modal = WebDriverWait(self.driver, 30).\
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_text_modal_init)))
            return text_modal.text
        except Exception as inst:
            print("Error: the view a windows modal", inst)

    def click_accept_modal(self):
        try:
            button_accept = WebDriverWait(self.driver, 20). \
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_button_accept_modal)))
            return button_accept.click()
        except Exception as inst:
            print("Error: By clicking on the button accept", inst)

    def close_page(self):
        self.driver.close()
