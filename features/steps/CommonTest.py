import time

from behave import step, given, when, then


class CommonTest:

    @then("앱종료")
    @when("앱종료")
    def terminate_app(context):
        context.mp.terimnate_app()
    @when("앱실행")
    def actavate_app(context):
        context.mp.activate_app()
