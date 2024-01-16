from data_gupy import Gupy
from form_rpa import Form
from dotenv import load_dotenv

import os

load_dotenv()

scrapy_grupy = Gupy()
scrapy_grupy.start_browser()
scrapy_grupy.select_url(os.getenv('URL_GUPY_GRUPOSEB'))
scrapy_grupy.pre_processament_page()
data_df = scrapy_grupy.run_scraper()

form = Form()
form.start_browser()
form.select_url(os.getenv('URL_FORM'))

for i, info in data_df.iterrows():
    form.data_insert(info['Localidade'], info['Cargo'], info['Efetividade'], info)
    