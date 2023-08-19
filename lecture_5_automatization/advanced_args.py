import argparse
parser = argparse.ArgumentParser()
parser.add_argument('amount',
                    type=float,
                    help="Initial currency amount")
parser.add_argument('--exchange_rate',
                    help="Initial currency amount",
                    type=float,
                    action='store',
                    default=1)
parser.add_argument('--verbose',
                    help="Verbosity Level",
                    action='store_true')

args = parser.parse_args()

result = args.amount * args.exchange_rate

if args.verbose:
    print(f'{args.amount} is converted using {args.exchange_rate}, and the result is {result}')
else:
    print(result)
