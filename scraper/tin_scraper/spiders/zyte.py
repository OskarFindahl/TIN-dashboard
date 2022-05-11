import json
import scrapy
from scrapinghub import ScrapinghubClient
from datetime import datetime 
import requests 

class ZyteSpider(scrapy.Spider):
    name = "zyte_spider"

    def __init__(self, *args, **kwargs):
        self._spiders = None
        self.client = None
        self.project = None
        super().__init__(*args, **kwargs)

    
    def start_requests(self):
        """ Initial request for scrapy to perform.
        Load settings and initialize ScrapingHubClient.

        Yields:
            _type_: _description_
        """''
        apikey = self.settings["SCRAPINGHUB_API_KEY"]
        self.root = self.settings["API_ROOT"]
        self.client = ScrapinghubClient(apikey)
        self.project = self.client.get_project(self.settings["SCRAPINGHUB_PROJECT_ID"])

        # Workaround, we do not need to make any request so we send a mock one and ignore it.
        yield scrapy.Request(url="http://localhost", meta={"ignore_request": True})

    def parse(self, response):
        item_array=[]
        for job, spider in self.all_jobs():
            error_count = len(job.logs.list(level = 'ERROR'))
            #Filtrera ut job som körs 
            item_count = len(job.items.list())
            finish_time = str(datetime.utcfromtimestamp(job.metadata._origin["finished_time"]/1000))
            
            item = {
                "spider": self.get_or_create_spider(spider.name),
                "num_items": item_count, 
                "num_errors": error_count,
                "id": job.key,
                "date": finish_time
            }
            item_array.append(item)
            
            print(item)
        # Flytta root url till settings
        requests.post(url="http://localhost:8000/zyte/job-data", json=item_array)


    def get_or_create_spider(self, spider_id):
        # Flytta root url till settings
        if self._spiders is None:
            self._spiders = requests.get(url="http://localhost:8000/zyte/spiders").json()
        for spider in self._spiders:
            if spider["id"] == spider_id:
                return spider["id"]
        spider = requests.post(url="http://localhost:8000/zyte/spiders", json={"id": spider_id}).json()   
        self._spiders.append(spider)
        return spider_id


    def all_jobs(self, limit=10):
        spiders = self.project.spiders
        for spider_dict in spiders.iter():
            spider = self.project.spiders.get(spider_dict['id'])
            jobs = spider.jobs.list()
            for job_dict in jobs[0: limit]: 
                job = self.project.jobs.get(job_dict['key'])
                yield job, spider