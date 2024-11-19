#!/usr/bin/env python3

import argparse
import subprocess

def main(args):
    with open(f'event-feed-{args.contest}.ndjson', 'w') as outfile:
        subprocess.run([
            'curl', '--no-buffer',
            '-u', f'{args.username}:{args.key}',
            '--speed-limit', '0',
            '--speed-time', '10',
            f'https://{args.hostname}/api/clics/contests/{args.contest}/event-feed'],
                       stdout=outfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--hostname', help='Hostname for the contest')
    parser.add_argument('-u', '--username', help='Kattis username')
    parser.add_argument('-k', '--key', help='API key')
    parser.add_argument('contest', help='Short name for the contest')
    args = parser.parse_args()

    main(args)

