from data_gupy import Gupy
from form_rpa import Form


scrapy_grupy = Gupy()
scrapy_grupy.start_browser()
scrapy_grupy.select_url('https://gruposeb.gupy.io/')
scrapy_grupy.pre_processament_page()
data_df = scrapy_grupy.run_scraper()

form = Form()
form.start_browser()
form.select_url('https://forms.office.com/pages/responsepage.aspx?id=QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u')

for i, info in data_df.iterrows():
    form.data_insert(info['Localidade'], info['Cargo'], info['Efetividade'], info)
    