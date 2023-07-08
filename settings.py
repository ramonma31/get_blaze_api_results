import pendulum

URL_DOUBLE_HISTORY = 'https://blaze.com/api/roulette_games/history'
URL_DOUBLE_CURREN = 'https://blaze.com/api/roulette_games/current'
URL_CRASH_CURRENT = 'https://blaze.com/api/crash_games/current'
URL_CRASH_HIRTORY = 'https://blaze.com/api/crash_games/history'

TIME_ZONE = pendulum.now().timezone_name

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
