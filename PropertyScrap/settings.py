from shutil import which
#selenium implementation 
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  
DOWNLOADER_MIDDLEWARES = {
            'PropertyScrap.middlewares.SeleniumMiddleware': 543,
}

#pipelines
ITEM_PIPELINES = {
    "PropertyScral.pipelines.PropertyScrapPipeline": 300,
}

#database settings
DATABASE = {
    "drivername": "postgres",
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "username": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASS"],
    "database": os.environ["POSTGRES_DB"],
}
LOG_LEVEL = "INFO"


#not to overload
DOWNLOAD_TIMEOUT = 540
DOWNLOAD_DELAY = 5
DEPTH_LIMIT = 10
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
    'scrapy.extensions.closespider.CloseSpider': 1
}     

BOT_NAME = 'PropertyScrap'

SPIDER_MODULES = ['PropertyScrap.spiders']
NEWSPIDER_MODULE = 'PropertyScrap.spiders'



# Obey robots.txt rules
ROBOTSTXT_OBEY = False

