from selenium.webdriver.common.by import By
from helpers.utilities import Utilities
from time import sleep


class Form:
    __slots__ = "robot", "logger"
    def __init__(self, log) -> None:
        self.robot = Utilities()
        self.logger = log

    def start_browser(self):
        try:
            self.robot.open_chrome()
            self.logger.info('Navegador FORM aberto.')            
        except Exception as e:
            raise

    def select_url(self, url):
        try:
            self.logger.info(f'Acessando URL {url}')
            self.robot.browser.get(url)
            self.robot.browser.delete_all_cookies()
        except Exception as e:
            raise
    
    def data_insert(self, text_location, text_office, text_effectiveness, info):
        
        self.logger.info(f'Inserindo dado de Localidade {text_location}')
        self.robot.browser.find_element(By.XPATH, "//input[@aria-labelledby='QuestionId_r62327b3de37b4158b46eb9bf1ff8b45d QuestionInfo_r62327b3de37b4158b46eb9bf1ff8b45d']").send_keys(text_location)
        sleep(0.2)
        self.logger.info(f'Inserindo dado de Cargo {text_office}')
        self.robot.browser.find_element(By.XPATH, "//input[@aria-labelledby='QuestionId_r28823796bb8b461195112faa4376895e QuestionInfo_r28823796bb8b461195112faa4376895e']").send_keys(text_office)
        sleep(0.2)
        
        yes_option = self.robot.browser.find_element(By.XPATH, "//span[@data-automation-value='Sim']")
        not_option = self.robot.browser.find_element(By.XPATH, "//span[@data-automation-value='Não']")        
        
        
        if text_effectiveness == 'Efetivo':
            self.logger.info(f'Inseriu dado de Efetividade: {text_effectiveness}')
            yes_option.click()
        else:
            self.logger.info(f'Inseriu dado de Efetividade: {text_effectiveness}')
            not_option.click()
            
        self.robot.browser.find_element(By.XPATH, "//button[@data-automation-id='submitButton']").click()
        
        self.robot.wait_element("//span[contains(text(), 'Enviar outra resposta')]")
        
        if not info.empty:
            self.logger.info('Enviando outra resposta!')                    
            self.robot.browser.find_element(By.XPATH, "//span[contains(text(), 'Enviar outra resposta')]").click()
            sleep(1)
        
        