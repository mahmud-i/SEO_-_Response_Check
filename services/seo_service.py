# services/seo_service.pyy

import os
import pandas as pd
from numpy.distutils.system_info import dfftw_info
from ydata_profiling import ProfileReport
from http.client import responses
from playwright.sync_api import sync_playwright
from pages.seo_page import SEOPage
from utils.comparator import compare_seo_data
from utils.report_styling import DataFrameStyler


class SEOService:
      def _init_(self): pass


      @staticmethod
      def fetch_dxp_seo_data(page_obj,page_response):
          page_state = page_response['status']
          if page_state == 200:
              seo_data={
               'http response': page_state,
               'title': page_obj.get_title(),
               'meta description':page_obj.get_meta_description(),
               'canonical link': page_obj.get_canonical_link(),
               'og:title': page_obj.get_og_title(),
               'og:description': page_obj.get_og_description(),
               'og:type': page_obj.get_og_type(),
               'og:site': page_obj.get_og_site(),
               'og:url': page_obj.get_og_url(),
               'og:image': page_obj.get_og_image(),
               'twitter:title': page_obj.get_twitter_title(),
               'twitter:description':page_obj.get_twitter_description(),
               'twitter:card': page_obj.get_twitter_card(),
               'twitter:image': page_obj.get_twitter_image()
              }
              return seo_data
          else:
              seo_data = {
               'http response': page_state,
               'title': page_obj.get_title(),
               'meta description':page_obj.get_meta_description(),
               'canonical link': page_obj.get_canonical_link(),
               'og:title': page_obj.get_og_title(),
               'og:description': page_obj.get_og_description(),
               'og:type': page_obj.get_og_type(),
               'og:site': page_obj.get_og_site(),
               'og:url': page_obj.get_og_url(),
               'og:image': page_obj.get_og_image(),
               'twitter:title': page_obj.get_twitter_title(),
               'twitter:description':page_obj.get_twitter_description(),
               'twitter:card': page_obj.get_twitter_card(),
               'twitter:image': page_obj.get_twitter_image()
              }
              return seo_data


      @staticmethod
      def fetch_canvas_seo_data(page_obj,page_response):
          page_state = page_response['status']
          if page_state == 200:
              seo_data = {
              'http response': page_state,
              'title': page_obj.get_title(),
              'meta description': page_obj.get_meta_description(),
              'canonical link': page_obj.get_canonical_link(),
              'og:title': page_obj.get_og_title(),
              'og:description': page_obj.get_og_description(),
              'og:type': page_obj.get_og_type_2(),
              'og:site': page_obj.get_og_site_2(),
              'og:url': page_obj.get_og_url_2(),
              'og:image': page_obj.get_og_image(),
              'twitter:title': page_obj.get_twitter_title(),
              'twitter:description': page_obj.get_twitter_description(),
              'twitter:card': page_obj.get_twitter_card(),
              'twitter:image': page_obj.get_twitter_image()
              }
              return seo_data
          else :
              seo_data = {
               'http response': page_state,
               'title': page_obj.get_title(),
               'meta description':page_obj.get_meta_description(),
               'canonical link': page_obj.get_canonical_link(),
               'og:title': page_obj.get_og_title(),
               'og:description': page_obj.get_og_description(),
               'og:type': page_obj.get_og_type(),
               'og:site': page_obj.get_og_site(),
               'og:url': page_obj.get_og_url(),
               'og:image': page_obj.get_og_image(),
               'twitter:title': page_obj.get_twitter_title(),
               'twitter:description':page_obj.get_twitter_description(),
               'twitter:card': page_obj.get_twitter_card(),
               'twitter:image': page_obj.get_twitter_image()
              }
              return seo_data

      @staticmethod
      def fetch_error_data():
              error_data = {
                  'http response': "Failed to process",
                  'title': "Failed to process",
                  'meta description': "Failed to process",
                  'canonical link': "Failed to process",
                  'og:title': "Failed to process",
                  'og:description': "Failed to process",
                  'og:type': "Failed to process",
                  'og:site': "Failed to process",
                  'og:url': "Failed to process",
                  'og:image': "Failed to process",
                  'twitter:title': "Failed to process",
                  'twitter:description': "Failed to process",
                  'twitter:card': "Failed to process",
                  'twitter:image': "Failed to process"
              }
              return error_data

      @staticmethod
      def run_tests(urls_to_check, prod_domain_url, stage_domain_url):

        def get_input(prompt):
            response = input(prompt).strip().upper()
            while response not in ['Y', 'N']:
                print("Invalid input. Please choose the right key (Y/N).")
                response = input(prompt).strip().upper()
            return response

        prod_tech = get_input("Is the prod site in DxP (Contentful)? (Y/N): ")
        one_trust = get_input("Is One Trust enabled in Staging? (Y/N): ")
        email_sgn = get_input("Is the Email Sign-up pop-up enabled in Staging? (Y/N): ")
        headless_chk = get_input("Do you want to run the test in Headless mode? (Y/N): ")
        page_ss = get_input("Do you want to capture screenshots of the pages? (Y/N): ")

        def check_headless():
            if headless_chk == 'Y':
                return True
            else:
                return False

        brand_name = prod_domain_url.replace('https://www.','').split('.')[0].strip().upper()
        print(f"Starting SEO & Response Crosschecked test for {brand_name}\n")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=check_headless())
            context = browser.new_context()

            stage_url_cred = stage_domain_url.replace('https://', 'https://kenvueuser:KenvuePassword2024!@')
            stage_domain_page = SEOPage(context.new_page())
            stage_domain_page.goto(stage_url_cred)
            stage_domain_page.wait_for_page_load()
            if one_trust == 'Y':
                stage_domain_page.accept_cookies('button#onetrust-accept-btn-handler')
            if email_sgn == 'Y':
                stage_domain_page.close_email_signup_popup('button.vds-self_flex-end')
            stage_domain_page.close_page()

            prod_domain_page = SEOPage(context.new_page())
            prod_domain_page.goto(prod_domain_url)
            prod_domain_page.wait_for_page_load()
            prod_domain_page.accept_cookies('button#onetrust-accept-btn-handler')
            if prod_tech == 'Y' :
                prod_domain_page.close_email_signup_popup('button.vds-self_flex-end')
            prod_domain_page.close_page()

            comparison_results = []
            stage_seo_meta_data = []
            seo_meta_data = []

            for url in urls_to_check:
                prod_status = {}
                stage_status = {}

                def log_response(response):
                     if response.url == url:
                        status_code = response.status
                        status_message = responses.get(status_code, "Unknown Status")
                        prod_status['status'] = status_code
                        prod_status['message'] = status_message
                        print(f"Response: {status_code} {status_message}")

                     elif response.url == stage_url:
                        status_code = response.status
                        status_message = responses.get(status_code, "Unknown Status")
                        stage_status['status'] = status_code
                        stage_status['message'] = status_message
                        print(f"Response: {status_code} {status_message}")

                try:
                    stage_url = url.replace(prod_domain_url, stage_domain_url)
                    prod_page = context.new_page()
                    stage_page = context.new_page()
                    stage_page.on("response", log_response)
                    prod_page.on("response", log_response)
                    prod_seo_page = SEOPage(prod_page)
                    stage_seo_page = SEOPage(stage_page)

                    print(f"Checking URL:\n Staging:{stage_url}\n Production: {url}")

                    stage_seo_page.goto(stage_url)
                    stage_seo_data = SEOService.fetch_dxp_seo_data(stage_seo_page, stage_status)
                    print(f"Stage_SEO Data: {stage_seo_data}\n")

                    prod_seo_page.goto(url)
                    if prod_tech == 'Y' :
                          prod_seo_data = SEOService.fetch_dxp_seo_data(prod_seo_page, prod_status)
                          print(f"Prod_SEO Data: {prod_seo_data}\n")
                          differences = compare_seo_data(stage_seo_data, prod_seo_data)
                          print(f"comparison: {differences}\n")
                          if page_ss == 'Y':
                            prod_seo_page.get_prod_ss(url, prod_domain_url, brand_name)

                    else :
                          prod_seo_data = SEOService.fetch_canvas_seo_data(prod_seo_page, prod_status)
                          print(f"Prod_SEO Data: {prod_seo_data}\n")
                          differences = compare_seo_data(prod_seo_data, stage_seo_data)
                          print(f"comparison: {differences}\n")
                          if page_ss == 'Y':
                            stage_seo_page.get_stage_ss(stage_url, stage_domain_url, brand_name)


                    row = {'URL': url, 'Staging URL': stage_url}
                    for key, value in differences.items():
                        row[f"{key}"] = value
                    comparison_results.append(row)
                    print('comparison Data Updated\n')

                    stage_row = {'URL': stage_url}
                    stage_row.update(stage_seo_data)  # Efficiently add all SEO data
                    stage_seo_meta_data.append(stage_row)
                    print('Stage SEO Data Updated\n')

                    row = {'URL': url }
                    row.update(prod_seo_data)  # Efficiently add all SEO data
                    seo_meta_data.append(row)
                    print('PROD SEO Data Updated\n')

                except Exception as e:
                    print(f"Error processing {url}: {e}")
                    crow_e = {'URL': url, 'Staging URL': stage_url}
                    row_e = {'URL': url }
                    err_data = SEOService.fetch_error_data()
                    row_e.update(err_data)
                    crow_e.update(err_data)

                    comparison_results.append(crow_e)
                    seo_meta_data.append(row_e)
                    stage_seo_meta_data.append(row_e)

                finally:
                    stage_seo_page.close_page()
                    prod_seo_page.close_page()

            context.browser.close()
            browser.close()

        print('Data Frame creation start\n')
        df_comparison = pd.DataFrame(comparison_results)
        df_production = pd.DataFrame(seo_meta_data)
        df_stage = pd.DataFrame(stage_seo_meta_data)

        print(df_comparison.columns)
        print(df_production.columns)
        print(df_stage.columns)

        excel_report_dct = f"Report/{brand_name}_Report/{brand_name}_excel_Report"
        os.makedirs(excel_report_dct, exist_ok=True)

        print('Excel report generation start\n')
        with pd.ExcelWriter(f"{excel_report_dct}/{brand_name}_SEO_&_Response_Check_report.xlsx") as writer:
            df_comparison.to_excel(writer, sheet_name='ComparisonResults', index=False)
            df_stage.to_excel(writer, sheet_name='Stage_SEO_Data', index=False)
            df_production.to_excel(writer, sheet_name='Prod_SEO_Data', index=False)

        print('HTML report generation start\n')
        html_report_dct = f"Report/{brand_name}_Report/{brand_name}_html_general_Report"
        os.makedirs(html_report_dct, exist_ok=True)

        df_comparison.to_html(f"{html_report_dct}/{brand_name}_SEO_&_Response_Comparison_Results_Report.html", index=False)
        df_stage.to_html(f"{html_report_dct}/{brand_name}_Stage_SEO_&_Response_Data_Report.html", index=False)
        df_production.to_html(f"{html_report_dct}/{brand_name}_Production_SEO_&_Response_Data_Report.html", index=False)

        print('HTML report profiling start\n')
        comparison_report = ProfileReport(df_comparison, title="Comparison Results Report", explorative=True)
        stage_report = ProfileReport(df_stage, title="Stage SEO Data Report", explorative=True)
        production_report = ProfileReport(df_production, title="Production SEO Data Report", explorative=True)

        print('HTML Profile report generation start\n')
        profile_report_dct = f"Report/{brand_name}_Report/{brand_name}_Data_Profiling_Report"
        os.makedirs(profile_report_dct, exist_ok=True)

        comparison_path = f"{profile_report_dct}/{brand_name}_SEO_&_Response_Comparison_Results_details_Report.html"
        comparison_report.to_file(comparison_path)
        stage_path = f"{profile_report_dct}/{brand_name}_Stage_SEO_&_Response_Data_details_Report.html"
        stage_report.to_file(stage_path)
        prod_path = f"{profile_report_dct}/{brand_name}_PROD_SEO_&_Response_Data_details_Report.html"
        production_report.to_file(prod_path)



        style_report_dct = f"Report/{brand_name}_Report/{brand_name}_Style_HTML_Report"
        os.makedirs(style_report_dct, exist_ok=True)

        print('Comparison HTML report styling and update start\n')
        styler_comparison = DataFrameStyler(df_comparison)
        styler_comparison.apply_styling_comparison_report()
        styler_comparison.generate_style_report(f"{style_report_dct}/{brand_name}_SEO_&_Response_Comparison_Results_details_Report.html")

        print('PROD Data HTML report styling and update start\n')
        styler_production = DataFrameStyler(df_production)
        styler_production.apply_styling_data_report()
        styler_production.generate_style_report(f"{style_report_dct}/{brand_name}_Production_SEO_&_Response_Data_details_Report.html")

        print('Stage Data HTML report styling and update start\n')
        styler_stage = DataFrameStyler(df_stage)
        styler_stage.apply_styling_data_report()
        styler_stage.generate_style_report(f"{style_report_dct}/{brand_name}_Stage_SEO_&_Response_Data_details_Report.html")
        print('All task Done\n\n')