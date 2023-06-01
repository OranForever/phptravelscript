from phptravel.phptravel import Phptravel


with Phptravel(teardown=True) as bot:
    bot.go_first_page()
    print("[Assertion Test] first name: Nick, last name: Cage, business name: Dior, email: nickcage@gmail.com")
    bot.enter_form("Nick", "Cage", "Dior", "nickcage@gmail.com")
    bot.go_first_page()
    print("[Assertion Test] first name: Nick, last name: Cage, business name: Dior, email: nickcage@gmail.com")
    bot.enter_form("Nick", "Cage", "Dior", "nickcagegmail.com")
    print('Exiting ...')