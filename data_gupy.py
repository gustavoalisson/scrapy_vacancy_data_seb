from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from helpers.utilities import Utilities
from time import sleep
import pandas as pd

from selenium.webdriver.support.ui import Select


class Gupy:
    __slots__ = "robot"
    def __init__(self) -> None:
        self.robot = Utilities()


    def start_browser(self):
        try:
            self.robot.open_chrome()
        except Exception as e:
            raise

    def select_url(self, url):
        try:
            self.robot.browser.get(url)
            self.robot.browser.delete_all_cookies()
        except Exception as e:
            raise
        
    def pre_processament_page(self):
        sleep(5)
        try:
            
            btn_initial_ok = self.robot.browser.find_element(By.XPATH, '//*[@id="radix-0"]/div[2]/button')
            btn_cookies_accept = self.robot.browser.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            
            if btn_initial_ok:
                btn_initial_ok.click()
            if btn_cookies_accept:
                btn_cookies_accept.click()
        except Exception as e:
            print(f'Erro ao capturar elemento da página. {e}')
            
        
    
    def scrapy_data(self, page):
        
        all_data = []
        
        print(f"Processando página {page}")
        
        
        element_data_listing_jobs = self.robot.browser.find_elements(By.XPATH,'//*[@id="job-listing"]/ul/li/a/div')
        
        for data in element_data_listing_jobs:
            office = data.find_element(By.XPATH, 'div[1]').text
            location = data.find_element(By.XPATH, 'div[2]').text
            effectiveness = data.find_element(By.XPATH, 'div[3]').text
            
            dict_data = {
                "Cargo": office,
                "Localidade": location,
                "Efetividade": effectiveness
            }
            
            all_data.append(dict_data)
            
        return all_data
        
        
    def run_scraper(self):
        
        processed_labels = []
        all_data = []
        try:
            while True:
                print('estou dentro do while')
                # Selecione os elementos de cada página
                page_elements = WebDriverWait(self.robot.browser, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[data-testid="pagination-page-button"]'))
                )
                
                # Processar os elementos da página atual
                for element in page_elements:
                    label = element.get_attribute('aria-label')
                    if label not in processed_labels:
                        data = self.scrapy_data(label)
                        print(data)
                        all_data.extend(data)
                        processed_labels.append(label)
                                    
                        try:
                            next_button = WebDriverWait(self.robot.browser, 10).until(
                                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="pagination-next-button"][aria-disabled="false"]'))
                                )
                        except Exception as e: 
                            ...
                    
                        if next_button.get_attribute('aria-disabled') == 'true':
                            print('Finalizado...')
                            
                            return False
                        
                        next_button.click()
                        # sleep(2)
        except Exception as e:
            print('erro durante a execução.')                    
        finally:
            df = pd.DataFrame(all_data)
            return df        

            
        