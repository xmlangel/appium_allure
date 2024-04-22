from base.BasePage import BasePage
import utilities.CustomLogger as cl
import pages.PageElements as el

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_main_form_button(self):
        BasePage.click_elements_by_xpath(self, el.button_liveness)
        cl.allure_logs("클릭 버튼")
    
    def click_main_form_id_verification_button(self):
        BasePage.click_elements_by_xpath(self, el.button_id_verification)
        cl.allure_logs("클릭 버튼2")
    
    def terimnate_app(self):
        BasePage.terminate_app(self)

    def activate_app(self):
        BasePage.activate_app(self)
