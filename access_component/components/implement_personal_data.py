from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from access_component.components.implementation_init_form import InitFormWeb


class PersonalData(InitFormWeb):
    __xpath_title_window = '//*[@id="contentSteps"]/div[1]/div/div[1]/h2'
    __xpath_cbx_type_doc = '//*[@id="contentSteps"]/div[1]/div/div[1]/app-formgenerator/div/div[1]/form-dropdown/div[1]/div[1]'
    __xpath_item_cbx_type_doc = '//*[@id="contentSteps"]/div[1]/div/div[1]/app-formgenerator/div/div[1]/form-dropdown/div[3]/div[1]'
    __xpath_txt_number_ci = '//*[@id="ci_2"]'
    __xpath_txt_complement = '//*[@id="ci_complemento_3"]'
    __xpath_txt_country_CI = '//*[@id="ci_emision_4"]'
    __xpath_cbx_extension = '//*[@id="contentSteps"]/div[1]/div/div[1]/app-formgenerator/div/div[5]/form-dropdown/div[1]/div[1]'
    __xpath_rb_expiration_undefined_yes = '//*[@id="ci_vencimiento_indefinido_option_1"]'
    __xpath_rb_expiration_undefined_not = '//*[@id="ci_vencimiento_indefinido_option_2"]'
    __xpath_calendar_date_expiration_ci = '//*[@id="ci_fecha_vencimiento_7"]'
    __xpath_button_continue = '//*[@id="content"]/div[2]/div[2]/button[1]'

    def get_title_insert_personal_data(self):
        try:
            text_window = WebDriverWait(self.driver, 30). \
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_title_window)))
            return text_window.text
        except Exception as inst:
            print("Error: get window insert personal data", inst)

    def deploy_cbx_type_ci(self):
        try:
            click_cbx_type_ci = WebDriverWait(self.driver, 30). \
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_cbx_type_doc)))
            return click_cbx_type_ci.click()
        except Exception as inst:
            print("Error: deploy cbx type ci", inst)

    def select_item_cbx_type_ci(self):
        try:
            click_item_cbx = WebDriverWait(self.driver, 30). \
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_item_cbx_type_doc)))
            return click_item_cbx.click()
        except Exception as inst:
            print("Error: Select item the cbx type ci", inst)

    def get_selected_item(self):
        try:
            item_selected = WebDriverWait(self.driver, 30). \
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_cbx_type_doc)))
            return item_selected.text
        except Exception as inst:
            print("Error:Item selected", inst)

    def insert_ci(self, ci):
        try:
            text_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                              ((By.XPATH, self.__xpath_txt_number_ci)))
            text_login.send_keys(ci)
        except Exception as inst:
            print("Error: Al ingresar el usuario en el campo de texto : ", inst)

    def get_text_ci(self):
        try:
            item_text_ci = WebDriverWait(self.driver, 30). \
                until(EC.element_to_be_clickable((By.XPATH, self.__xpath_txt_number_ci)))
            return item_text_ci.text
        except Exception as inst:
            print("Error: get text in input document", inst)

    def state_button_continue(self):
        pass

    def insert_complement(self):
        pass

    def insert_country_ci(self):
        pass

    def deploy_cbx_extension(self):
        pass

    def select_item_cbx_extension(self):
        pass
