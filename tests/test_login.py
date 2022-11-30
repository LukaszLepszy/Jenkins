import pytest

from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("login", ['standard_user', 'problem_user'])
    def test_login(self, login):
        obj = HomePage(self.driver)
        obj.go_to_website()
        obj.put_data_input(login)
        obj.click_button()
        assert obj.get_text_css(obj.header_text) == 'PRODUCTSs'