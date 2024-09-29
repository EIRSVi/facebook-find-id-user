import pyfiglet
from colorama import Fore, init
import time
import os
import requests, re, argparse

# Initialize Colorama
init(autoreset=True)

def print_colored_logo():
    # Generate ASCII art for the logo with a modern font
    logo = pyfiglet.figlet_format("SRIEVi", font="slant")

    # Center the logo in the terminal
    terminal_width = os.get_terminal_size().columns
    centered_logo = "\n".join(line.center(terminal_width) for line in logo.splitlines())

    # Colors for the gradient effect (cyber-like appearance)
    colors = [Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]

    # Apply a glowing effect to each character in the logo
    print("\n")  # Add spacing before the logo
    for i, char in enumerate(centered_logo):
        if char.strip():  # Apply color only to non-space characters
            print(colors[i % len(colors)] + char, end='', flush=True)
            time.sleep(0.02)  # Slight delay to create a glowing effect
        else:
            print(char, end='', flush=True)
    print("\n")  # New line after the logo

def print_welcome():
    # Call the function to print the colored logo
    print_colored_logo()
    
    # Welcome message
    welcome_message = f"{Fore.LIGHTBLUE_EX}Welcome to the Facebook Find ID User \n"
    terminal_width = os.get_terminal_size().columns
    centered_message = welcome_message.center(terminal_width)
    print(centered_message)

    # Updated GitHub and social links
    developer_info = f"Support us {Fore.LIGHTGREEN_EX}@eirsvi "
    centered_developer = developer_info.center(terminal_width)
    print(centered_developer)

    social_links = f"{Fore.LIGHTRED_EX} GitHub | X | YouTube  \n"
    centered_social_links = social_links.center(terminal_width)
    print(centered_social_links)

    # Example URL without centering
    example_url = f"EXAMPLE URL: Username OR Link Profile: {Fore.LIGHTYELLOW_EX}zuck"
    print(example_url)
    
    print()  # Add an extra newline for spacing

if __name__ == "__main__":
    print_welcome()


# Argument Parser 
parser = argparse.ArgumentParser()
parser.add_argument("username", help="Provide the Facebook username (e.g., username from https://www.facebook.com/username).")

args = parser.parse_args()
username = args.username

# Construct the full Facebook URL
url = f"https://www.facebook.com/{username}"

# FB Identification
byte_obj = b'"userID":"([0-9]+)"'
id_req = re.compile(byte_obj)
page = requests.get(url)
fb_list = id_req.findall(page.content)

if fb_list:
    # Decoding the user ID from the list of bytes
    fbid = fb_list[0].decode()

    # Result
    print(f"{Fore.LIGHTGREEN_EX}[*] The Facebook ID for this account is: {Fore.LIGHTMAGENTA_EX}{fbid}")
else:
    print(f"{Fore.LIGHTRED_EX}[!] No Facebook ID found. Check if the username is correct.")
