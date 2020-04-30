"""
Gets a job from the server and handles the job based on the type of job
"""
import argparse

from c20_client.do_client_job import do_multiple_job


def main():
    parser = argparse.ArgumentParser(
        description="get files from regulations.gov")
    parser.add_argument("API_key", help="api key for regulations.gov")
    args = parser.parse_args()
    do_multiple_job(args.API_key)


if __name__ == '__main__':
    main()
