from phptravel.phptravel import Phptravel
from phptravel.constants import BASE_URL


with Phptravel(teardown=True) as bot:

    print("[Assertion Test] Testing url " + BASE_URL)
    bot.go_first_page()
    if not "Phptravels" in bot.title:
        raise Exception("[Assertion Test] Fail, Unable to load page")
    else:
        print("[Assertion Test] Success")
    #bot.test_Buttons()
    bot.test_dropdown()
    print("[Assertion Test] first name: Nick, last name: Cage, business name: Dior, email: nickcage@gmail.com")
    #bot.enter_form("Nick", "Cage", "Dior", "nickcage@gmail.com")
    #bot.go_first_page()
    print("[Assertion Test] first name: Nick, last name: Cage, business name: Dior, email: nickcage@gmail.com")
    #bot.enter_form("Nick", "Cage", "Dior", "nickcagegmail.com")
    print('Exiting ...')