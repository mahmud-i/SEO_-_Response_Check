import os
from playwright.sync_api import Page


class SEOPage:
    def __init__(self, page: Page):
        self.page = page

    def accept_cookies(self, selector):
         # Adjust the selector based on the actual cookie popup on your site
        self.wait_for_content_load(selector)
        accept_button = self.page.query_selector(selector)  # Example selector
        if accept_button:
            accept_button.click()

    def close_email_signup_popup(self, selector):
        # Adjust the selector based on the actual email signup popup on your site
        self.wait_for_content_load(selector)
        self.close_button(selector)

    def close_button(self, selector):
        # Adjust the selector based on the actual email signup popup on your site
        close_button = self.page.locator(selector)  # Example selector
        if close_button:
             close_button.click()

    def wait_for_time(self, timeout):
        self.page.wait_for_timeout(timeout)

    def get_stage_ss(self, url, domain_url, brand_name):
        self.wait_for_time(50000)
        sanitized_url = os.path.basename(url)
        # Define the fixed directory and create the file path
        file_path = f"Report/{brand_name}_Report/Stage_page_SS/{sanitized_url}.png"
        # Take the screenshot
        self.page.screenshot(path=file_path, full_page=True)
        print("Stage Page SS Captured\n")

    def get_prod_ss(self, url, domain_url, brand_name):
        sanitized_url = os.path.basename(url)
        # Define the fixed directory and create the file path
        file_path = f"Report/{brand_name}_Report/Prod_page_SS/{sanitized_url}.png"
        # Take the screenshot
        self.page.screenshot(path=file_path, full_page=True)
        print("PROD Page SS Captured\n")


    def wait_for_content_load(self, selector):
        self.page.wait_for_selector(selector, timeout=10000)

    def goto(self, url):
        self.page.goto(url)
        self.wait_for_page_load()

    def close_page(self):
        self.page.close()

    def wait_for_page_load(self, timeout=10000):
        self.page.wait_for_load_state('load', timeout=timeout)

    def get_image_data(self):
        images = self.page.query_selector_all('img')
        return images if images else None


    def get_title(self):
        return self.page.title()

    def get_meta_description(self):
        element = self.page.query_selector("meta[name='description']")
        return element.get_attribute('content') if element else None

    def get_canonical_link(self):
        element = self.page.query_selector("link[rel='canonical']")
        return element.get_attribute('href') if element else None

    def get_og_title(self):
        element = self.page.query_selector("meta[property='og:title']")
        return element.get_attribute('content') if element else None

    def get_og_description(self):
        element = self.page.query_selector("meta[property='og:description']")
        return element.get_attribute('content') if element else None

    def get_og_type(self):
        element = self.page.query_selector("meta[name='og:type']")
        return element.get_attribute('content') if element else None

    def get_og_site(self):
        element = self.page.query_selector("meta[name='og:site_name']")
        return element.get_attribute('content') if element else None

    def get_og_url(self):
        element = self.page.query_selector("meta[name='og:url']")
        return element.get_attribute('content') if element else None

    def get_og_image(self):
        element = self.page.query_selector("meta[property='og:image']")
        image_path = element.get_attribute('content') if element else None
        image_name = os.path.basename(image_path) if image_path else None
        return image_name if element else None


    # to check with Canvas PROD
    def get_og_type_2(self):
        element = self.page.query_selector("meta[property='og:type']")
        return element.get_attribute('content') if element else None

    def get_og_site_2(self):
        element = self.page.query_selector("meta[property='og:site_name']")
        return element.get_attribute('content') if element else None

    def get_og_url_2(self):
        element = self.page.query_selector("meta[property='og:url']")
        return element.get_attribute('content') if element else None

    # to check with Canvas PROD




    def get_twitter_title(self):
        element = self.page.query_selector("meta[name='twitter:title']")
        return element.get_attribute('content') if element else None

    def get_twitter_description(self):
        element = self.page.query_selector("meta[name='twitter:description']")
        return element.get_attribute('content') if element else None

    def get_twitter_card(self):
        element = self.page.query_selector("meta[name='twitter:card']")
        return element.get_attribute('content') if element else None

    def get_twitter_image(self):
        element = self.page.query_selector("meta[name='twitter:image']")
        image_path = element.get_attribute('content') if element else None
        image_name = os.path.basename(image_path) if image_path else None
        return image_name if element else None


