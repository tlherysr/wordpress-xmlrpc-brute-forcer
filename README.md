# WordPress XML-RPC Brute Forcer
This mini project demonstrates a brute force attack leveraging the XML-RPC `wp.getUsersBlogs` method in WordPress. While outdated, this vulnerability can still be exploited if proper security measures aren’t in place.

---

## ⚠️ Disclaimer 
This tool is for **authorized penetration testing** and **educational purposes only**. Misuse of this script may lead to legal consequences. Use responsibly and only on systems you own or have explicit permission to test.  

---

## Features  

- Checks if the xmlrpc.php is enabled and exploitable on the given URL.
- Exploits the `wp.getUsersBlogs` method to test multiple credentials.
- Identifies weak credentials on vulnerable WordPress installations.

---

## Installation 
### Install with Poetry

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/xmlrpc-bruteforce.git  
   cd xmlrpc-bruteforcer
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Run the script
   ```bash
   poetry run python main.py --username <target-username> --target <target-url> --wordlist <wordlist-path> --processes 3 --verbose
   ```

### Install with requirements.txt

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/xmlrpc-bruteforce.git  
   cd xmlrpc-bruteforcer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script
   ```bash
   python main.py --username <target-username> --target <target-url> --wordlist <wordlist-path> --processes 3 --verbose
   ```

---  

## Usage Example
```bash
python main.py --username admin --target http://example.com/xmlrpc.php --wordlist ./data/passwords.txt --processes 3 --verbose
```
### Arguments  
- --username: The admin username to be targeted.
- --target: The target WordPress site with the xmlrpc.php endpoint.
- --wordlist: Path to the wordlist containing possible usernames and passwords.
- --processes: Number of processes for parallel requests. By default it is 3.
- --verbose: To enable verbosity and show all the tried passwords in the wordlist.

## Prevention

To secure WordPress installations:

- Disable xmlrpc.php if not needed.
- Use strong and unique passwords.
- Implement rate limiting or WAFs.

## License
This project is licensed under the MIT License. 

Let me know if you'd like adjustments or additional details!
@TlhErysr