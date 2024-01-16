from data_gupy import Gupy
from form_rpa import Form
from dotenv import load_dotenv
from log_data.logger import LogGenerator

import os

load_dotenv()

log_instance = LogGenerator()
logger = log_instance.setup_logger()

scrapy_grupy = Gupy(logger)
scrapy_grupy.start_browser()
scrapy_grupy.select_url(os.getenv('URL_GUPY_GRUPOSEB'))
scrapy_grupy.pre_processament_page()
data_df = scrapy_grupy.run_scraper()

form = Form(logger)
form.start_browser()
form.select_url(os.getenv('URL_FORM'))

for i, info in data_df.iterrows():
    
    info['Localidade'] = info['Localidade'] if info['Localidade'] else "Dado vazio no site."
    info['Cargo'] = info['Cargo'] if info['Cargo'] else "Dado vazio no site."
    info['Efetividade'] = info['Efetividade'] if info['Efetividade'] else "Dado vazio no site."
    
    form.data_insert(info['Localidade'], info['Cargo'], info['Efetividade'], info)

logger.info('Inserção de dados concluída!!!')