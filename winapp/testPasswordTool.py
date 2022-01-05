import pytest_check as check
from winapp.passwordTool import PasswordTool

pwd = "XXX"


def test_generate_pwd(parameters):
    try:
        pwdTool = PasswordTool()

        pwdTool.keyin_login_password(pwd)
        pwdTool.click_ok()

        pwdTool.driver.switch_to.window(pwdTool.get_all_windows()[0])

        pwdTool.keyin_serialsn(parameters['unit'])
        # pwdTool.keyin_password("xxx")  # not need, this will be generated automatically after click Generate button
        pwdTool.click_generate()
    except Exception as ex:
        check.equal(True, False)
        print("test_generate_pwd Exception " + str(ex))
    finally:
        pwdTool.teardown()
