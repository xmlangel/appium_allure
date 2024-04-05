import time

from behave import step,given,when,then

from base.BasePage import BasePage
from pages.MainPage import MainPage

class LivenessTest:

    @given("초기화")
    def class_objects(context):
        context.mp = MainPage(context.driver)
        context.bp = BasePage(context.driver)
       
    @when("APP 클릭")
    def click_contactform_page(context):
        context.mp.click_main_form_button()

    @then("APP 타이틀 표시")
    def show_contactform_page(context):
        context.lv.show_title()