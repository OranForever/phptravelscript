from phptravel.phptravel import Phptravel

with Phptravel(teardown=True) as bot:
    bot.go_first_page()
    print('Exiting ...')