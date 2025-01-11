import requests
import time

import random

# Console colors for styling
PURPLE = "\033[35m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# Banner and tagline
ascii_banner = f"""
{PURPLE}    ______      __        __  ______                 __
   / ____/___  / /_____  / /_/ ____/______  ______  / /_____
  / /_  / __ \/ //_/ _ \/ __/ /   / ___/ / / / __ \/ __/ __ \\
 / __/ / /_/ / ,< /  __/ /_/ /___/ /  / /_/ / /_/ / /_/ /_/ /
/_/    \____/_/|_|\___/\__/\____/_/   \__, / .___/\__/\____/
                                     /____/_/               {RESET}
"""

tagline = f"""
{YELLOW} +-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+
 |A|n|y|o|n|e| |w|a|n|t| |d|o| |s|o|m|e| |d|o|n|a|t|i|o|n|
 +-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+ {RESET}
"""

# Display banner and links
print(f"{GREEN}{'=' * 70}{RESET}")
print(f"{ascii_banner}")
print(f"{tagline}")
print(f"{GREEN}{'=' * 70}{RESET}")
print(f"{YELLOW}{BOLD}{UNDERLINE}Telegram: https://t.me/foketcrypto{RESET}")
print(f"{RED}{BOLD}{UNDERLINE}YouTube: https://youtube.com/@foketcrypto{RESET}")
print(f"{GREEN}{'=' * 70}{RESET}")

# Function to send requests
def send_request(count, energy, token, max_retries=3):
    url = 'https://api.mokl.io/public/api/clicker/tap'
    headers = {
        'authority': 'api.mokl.io',
        'accept': 'application/json',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://play.mokl.io',
        'referer': 'https://play.mokl.io/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    data = {
        'count': count,
        'energy': energy,
        'timestamp': int(time.time()),
      
    }

    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.post(url, headers=headers, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            attempt += 1
            print(f"{RED}Request timed out. Retrying... Attempt {attempt}/{max_retries}{RESET}")
            time.sleep(2)
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    return {"error": f"Request failed after {max_retries} attempts."}

# Read tokens from file
with open('data.txt', 'r') as file:
    tokens = [line.strip() for line in file.readlines()]

while True:
    for token in tokens:
        print(f"\n{BLUE}Processing token: {token}{RESET}")
        for i in range(4):
            count = random.randint(130, 150)  # Random count
            energy = 500
            response = send_request(count, energy, token)

            if "error" in response:
                print(f"{RED}Error on request {i + 1}/4: {response['error']}{RESET}")
            else:
                print(f"{GREEN}Success on request {i + 1}/4: {response}{RESET}")

            delay = random.uniform(2, 5)
            print(f"{YELLOW}Calculated delay: {delay:.2f} seconds{RESET}")
            time.sleep(delay)

        print(f"{BLUE}Completed 4 requests for token {token}.{RESET}")

    sleep_time = random.uniform(8.1 * 60, 8.5* 60)
    print(f"{RED}Sleeping for {sleep_time:.2f} seconds before processing next batch of tokens...{RESET}")
    time.sleep(sleep_time)