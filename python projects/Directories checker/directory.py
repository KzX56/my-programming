import requests
import sys

def make_request(url):
    """
    attempts to make an HTTP GET request to the given URL.

    args:
        url (str): The full URL to request.

    returns:
        requests.Response or None: The response object if successful, None otherwise.
    """
    try:
        # It's safer to expect URLs with schemes (http:// or https://).
        # If the input doesn't have one, we'll assume https:// for this tool.
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return requests.get(url, timeout=5) # Added a timeout for better performance
    except requests.exceptions.ConnectionError:
        print(f"[-] Connection error for: {url}")
        return None
    except requests.exceptions.Timeout:
        print(f"[-] Request timed out for: {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"[-] An error occurred during the request to {url}: {e}")
        return None

def main():
   
    target_url = input('[*] Enter Target URL (e.g., example.com): ').strip()
    if not target_url:
        print("[-] Target URL cannot be empty. Exiting.")
        sys.exit(1)

    wordlist_file = input('[*] Enter Name of the Wordlist File (e.g., dir_list.txt): ').strip()
    if not wordlist_file:
        print("[-] Wordlist file name cannot be empty. Exiting.")
        sys.exit(1)

    print(f"\n[*] Starting directory brute-force on: {target_url} using {wordlist_file}")
    print("-" * 50)

    try:
        with open(wordlist_file, 'r') as f:
            for line in f:
                directory = line.strip()
                if directory:  # Ensure the line is not empty
                    full_url = f"{target_url}/{directory}"
                    response = make_request(full_url)
                    if response and response.status_code == 200: # Only report successful (200 OK) responses
                        print(f"[+] Discovered Directory: {full_url} (Status: {response.status_code})")
                    elif response:
                        print(f"[*] Checked: {full_url} (Status: {response.status_code})")
    except FileNotFoundError:
        print(f"[-] Error: The file '{wordlist_file}' was not found. Please ensure it's in the correct directory.")
        sys.exit(1)
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        sys.exit(1)

    print("-" * 50)
    print("[*] Directory brute-force completed.")

if __name__ == "__main__":
    main()
