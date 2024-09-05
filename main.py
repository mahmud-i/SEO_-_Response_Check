# main.py

from utils.csv_reader import get_urls_from_csv
from services.seo_service import SEOService


def main():
    file_path = input("Enter your .csv file path where all urls are listed for check(ex: a/b/c/df.csv): ")
    urls_to_check = get_urls_from_csv(file_path)
    prod_domain_url = input("Please write the PROD site Domain Link: ")
    stage_domain_url = input("Please write the Staging site Domain Link: ")

    service = SEOService()
    service.run_tests(urls_to_check, prod_domain_url, stage_domain_url)



if __name__ == "__main__":
        main()