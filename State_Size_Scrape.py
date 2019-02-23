#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scrapy.spiders import Spider

class Scraper(Spider):
    name = 's1'
    #only allows spider to go to this webpage.
    allowed_domains = ["netstate.com"]
    start_urls = [ "http://www.netstate.com/states/tables/st_size.htm" ]
    
    #Parse function to read the webpage
    def parse(self, response): #response is the webpage being sent back as a python data structure.
        '''
        Read the State, total sq miles, land sq miles and water sq miles
        '''
        rows = response.xpath("/html/body/table/tbody/tr[2]/td[@id='contentcolumn']/table[@id='stripedtable']/tbody[2]") 
        basePath = 'http://www.netstate.com'
        items = []
        item = {}
        item['State'] = rows.xpath("//tr[1]/td[2]/text()").get()
        print(item['State'])
        item['Total_Sq_Miles'] = rows.xpath("./tr[1]/td[3]").get()
        print(item['Total_Sq_Miles'])
        items.append(item)
#         for row in rows: #go through each item and build up a dictionary of info.  Add to items
#             item = {}
#             item['State'] = row.xpath("./tr[1]/td[2]/text()").extract()
#             #item['Total_Sq_Miles'] = row.xpath("./tr[1]/td[3]").extract()
#             #item['Land_Sq_Miles'] = row.xpath("./tr[1]/td[5]").extract()
#             #item['Water_Sq_Miles'] = row.xpath("./tr[1]/td[7]").extract()
#             items.append(item)
        return items

