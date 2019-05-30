import argparse 

import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=argparse.FileType('r'),
                    help="configuration of the mail server")
    parser.add_argument("emails", type=argparse.FileType('r'),
                    help="csv of emails")
    parser.add_argument("message", type=argparse.FileType('r'),
                    help="message body content")
    parser.add_argument("--dry-run", action="store_true",
                    help="performs a dryrun and does not ")
    args = parser.parse_args()

    return args

def load_emails(file):
	df = pd.read_csv(file)
	df = df.drop_duplicates(subset=['emails'], keep='first')
	return df

def validate_emails(df):
	pass

def main():
    df = load_emails("emails.csv")
    print(df)

	# args = parse_args()
    message = """\
    From: contact@akordhomes.com\n\
    To: robillard.matt@gmail.com\n\
    Subject: Real Estate Market Survey\n\


    This message is sent from Python.\

    Best, 

    Matt
    Co-founder
    """
    
    #print(message)

if __name__ == '__main__':
	main()