from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.options import Options
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """

    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone XR"})
    # context.driver = webdriver.Chrome(options=options)


    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')  # Firefox uses '--headless' instead of 'headless'
    # context.driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))


    ## BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'kam_Peoa08'
    # bs_key = 'NjaN6Jr5yrjnC47mEhj5'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #     'browserName': 'edge',
    #     'sessionName': 'user can navigate to Connect the Company page',
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # from selenium.webdriver.common.options import ArgOptions

    # BrowserStack options for iPhone 12 Pro
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'kam_Peoa08'
    bs_key = 'NjaN6Jr5yrjnC47mEhj5'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "deviceName" : "iPhone 12 Pro",
        "osVersion" : "18",
        'browserName': 'safari',
        'sessionName': 'Mobile user can navigate to Connect the Company page',
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


#Chrome emulation code:

    # from selenium import webdriver
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Chrome(options=chrome_options)

    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    #     "clientHints": {"platform": "Android", "mobile": True}}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # # driver = webdriver.Chrome(chrome_options=chrome_options)



    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait=WebDriverWait(context.driver, 15)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()


