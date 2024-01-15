from data_gupy import Gupy


scrapy_grupy = Gupy()
scrapy_grupy.start_browser()
scrapy_grupy.select_url('https://gruposeb.gupy.io/')
scrapy_grupy.pre_processament_page()
scrapy_grupy.run_scraper()