from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from behave import *
# from webdriver_manager.chrome import ChromeDriverManager
import time
import  datetime


@given('Launch The Google Chrome Browser')
def launchbrowser(context):
    # context.driver = webdriver.Chrome(ChromeDriverManager().install())

    context.driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@when('Open The Subscribe STCTV Site')
def opensite(context):
    context.driver.get("https://subscribe.stctv.com/sa-en")
    time.sleep(5)


@then('Verify Countries Names From Span')
def verifycountries(context):
    context.driver.find_element(By.XPATH, '//a[@id="country-btn"]').click()
    time.sleep(2)

    Bahrain = context.driver.find_element(By.XPATH, '//span[@id="bh-contry-lable"]').text
    assert Bahrain == 'Bahrain'

    KSA = context.driver.find_element(By.XPATH, '//span[@id="sa-contry-lable"]').text
    assert KSA == 'KSA'

    Kuwait = context.driver.find_element(By.XPATH, '//span[@id="kw-contry-lable"]').text
    assert Kuwait == 'Kuwait'


@then('Click on KSA Country')
def ksacountry(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='https://subscribe.stctv.com/sa-en']").click()
    time.sleep(2)


@then('Subscription Packages Validations For KSA Country')
def subscriptionksacountry(context):
    LITE = context.driver.find_element(By.XPATH, '//strong[@id="name-lite"]').text
    assert LITE == 'LITE'

    KSA_LITE_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="lite-selection"]').text
    assert KSA_LITE_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="lite-selection"]').click()
    time.sleep(5)

    KSA_STC_PRICE_L = context.driver.find_element(By.XPATH, '//span[@id="stc-price"]')
    KSA_STC_PRICE_VALUE = KSA_STC_PRICE_L.text
    assert KSA_STC_PRICE_VALUE == 'Starting: 15.00 SAR'
    time.sleep(2)

    KSA_VISA_PRICE_L = context.driver.find_element(By.XPATH, '//span[@id="cc_ksa-price"]')
    KSA_VISA_PRICE_VALUE = KSA_VISA_PRICE_L.text
    assert KSA_VISA_PRICE_VALUE == 'Starting: 20.00 SAR'
    time.sleep(2)

    context.driver.get("https://subscribe.stctv.com/sa-en")
    time.sleep(5)

    CLASSIC = context.driver.find_element(By.XPATH, '//strong[@id="name-classic"]').text
    assert CLASSIC == 'CLASSIC'

    KSA_CLASSIC_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="classic-selection"]').text
    assert KSA_CLASSIC_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="classic-selection"]').click()
    time.sleep(5)

    KSA_STC_PRICE_C = context.driver.find_element(By.XPATH, '//span[@id="stc-price"]')
    KSA_STC_PRICE_VALUE = KSA_STC_PRICE_C.text
    assert KSA_STC_PRICE_VALUE == 'Starting: 25.00 SAR'
    time.sleep(2)

    KSA_VISA_PRICE_C = context.driver.find_element(By.XPATH, '//span[@id="cc_ksa-price"]')
    KSA_VISA_PRICE_VALUE = KSA_VISA_PRICE_C.text
    assert KSA_VISA_PRICE_VALUE == 'Starting: 40.00 SAR'
    time.sleep(2)

    context.driver.get("https://subscribe.stctv.com/sa-en")
    time.sleep(5)

    PREMIUM = context.driver.find_element(By.XPATH, '//strong[@id="name-premium"]').text
    assert PREMIUM == 'PREMIUM'

    KSA_PREMIUM_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="premium-selection"]').text
    assert KSA_PREMIUM_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="premium-selection"]').click()
    time.sleep(5)

    KSA_STC_PRICE_P = context.driver.find_element(By.XPATH, '//span[@id="stc-price"]')
    KSA_STC_PRICE_VALUE = KSA_STC_PRICE_P.text
    assert KSA_STC_PRICE_VALUE == 'Starting: 60.00 SAR'
    time.sleep(2)

    KSA_VISA_PRICE_P = context.driver.find_element(By.XPATH, '//span[@id="cc_ksa-price"]')
    KSA_VISA_PRICE_VALUE = KSA_VISA_PRICE_P.text
    assert KSA_VISA_PRICE_VALUE == 'Starting: 60.00 SAR'
    time.sleep(2)


@then('Click on BAHRAIN Country')
def bahraincountry(context):
    context.driver.get("https://subscribe.stctv.com/sa-en")
    time.sleep(5)

    context.driver.find_element(By.XPATH, '//a[@id="country-btn"]').click()
    time.sleep(2)

    context.driver.find_element(By.CSS_SELECTOR, "a[href*='https://subscribe.stctv.com/bh-en']").click()
    time.sleep(2)


@then('Subscription Packages Validations For BAHRAIN Country')
def subscriptionbahraincountry(context):
    LITE_B = context.driver.find_element(By.XPATH, '//strong[@id="name-lite"]').text
    assert LITE_B == 'LITE'

    BAHRAIN_LITE_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="lite-selection"]').text
    assert BAHRAIN_LITE_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="lite-selection"]').click()
    time.sleep(5)

    BAHRAIN_STC_PRICE_L = context.driver.find_element(By.XPATH, '//span[@id="vb-price"]')
    BAHRAIN_STC_PRICE_VALUE = BAHRAIN_STC_PRICE_L.text
    assert BAHRAIN_STC_PRICE_VALUE == 'Starting: 2.00 BHD'
    time.sleep(2)

    BAHRAIN_VISA_PRICE_L = context.driver.find_element(By.XPATH, '//span[@id="cc_brn-price"]')
    BAHRAIN_VISA_PRICE_VALUE = BAHRAIN_VISA_PRICE_L.text
    assert BAHRAIN_VISA_PRICE_VALUE == 'Starting: 4.80 USD'
    time.sleep(2)

    context.driver.get("https://subscribe.stctv.com/bh-en")
    time.sleep(5)

    CLASSIC_B = context.driver.find_element(By.XPATH, '//strong[@id="name-classic"]').text
    assert CLASSIC_B == 'CLASSIC'

    BAHRAIN_CLASSIC_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="classic-selection"]').text
    assert BAHRAIN_CLASSIC_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="classic-selection"]').click()
    time.sleep(5)

    BAHRAIN_STC_PRICE_B = context.driver.find_element(By.XPATH, '//span[@id="vb-price"]')
    BAHRAIN_STC_PRICE_VALUE = BAHRAIN_STC_PRICE_B.text
    assert BAHRAIN_STC_PRICE_VALUE == 'Starting: 3.00 BHD'
    time.sleep(2)

    BAHRAIN_VISA_PRICE_B = context.driver.find_element(By.XPATH, '//span[@id="cc_brn-price"]')
    BAHRAIN_VISA_PRICE_VALUE = BAHRAIN_VISA_PRICE_B.text
    assert BAHRAIN_VISA_PRICE_VALUE == 'Starting: 9.60 USD'
    time.sleep(2)

    context.driver.get("https://subscribe.stctv.com/bh-en")
    time.sleep(5)

    PREMIUM_B = context.driver.find_element(By.XPATH, '//strong[@id="name-premium"]').text
    assert PREMIUM_B == 'PREMIUM'

    BAHRAIN_PREMIUM_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="premium-selection"]').text
    assert BAHRAIN_PREMIUM_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="premium-selection"]').click()
    time.sleep(5)

    BAHRAIN_STC_PRICE_P = context.driver.find_element(By.XPATH, '//span[@id="vb-price"]')
    BAHRAIN_STC_PRICE_VALUE = BAHRAIN_STC_PRICE_P.text
    assert BAHRAIN_STC_PRICE_VALUE == 'Starting: 6.00 BHD'
    time.sleep(2)

    BAHRAIN_VISA_PRICE_P = context.driver.find_element(By.XPATH, '//span[@id="cc_brn-price"]')
    BAHRAIN_VISA_PRICE_VALUE = BAHRAIN_VISA_PRICE_P.text
    assert BAHRAIN_VISA_PRICE_VALUE == 'Starting: 14.40 USD'
    time.sleep(2)


@then('Click on KUWAIT Country')
def kuwaitcountry(context):
    context.driver.get("https://subscribe.stctv.com/bh-en")
    time.sleep(5)

    context.driver.find_element(By.XPATH, '//a[@id="country-btn"]').click()
    time.sleep(2)

    context.driver.find_element(By.CSS_SELECTOR, "a[href*='https://subscribe.stctv.com/kw-en']").click()
    time.sleep(2)


@then('Subscription Packages Validations For KUWAIT Country')
def subscriptionkuwaitcountry(context):
    LITE_K = context.driver.find_element(By.XPATH, '//strong[@id="name-lite"]').text
    assert LITE_K == 'LITE'

    KUWAIT_LITE_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="lite-selection"]').text
    assert KUWAIT_LITE_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="lite-selection"]').click()
    time.sleep(5)

    KUWAIT_STC_PRICE_L = context.driver.find_element(By.XPATH, '//span[@id="vk-price"]')
    KUWAIT_STC_PRICE_VALUE = KUWAIT_STC_PRICE_L.text
    assert KUWAIT_STC_PRICE_VALUE == 'Starting: 1.20 KWD'
    time.sleep(2)

    KUWAIT_VISA_PRICE_L = context.driver.find_element(By.XPATH, '//span[@id="cc_kuw-price"]')
    KUWAIT_VISA_PRICE_VALUE = KUWAIT_VISA_PRICE_L.text
    assert KUWAIT_VISA_PRICE_VALUE == 'Starting: 4.80 USD'
    time.sleep(2)

    context.driver.get("https://subscribe.stctv.com/kw-en")
    time.sleep(5)

    CLASSIC_K = context.driver.find_element(By.XPATH, '//strong[@id="name-classic"]').text
    assert CLASSIC_K == 'CLASSIC'

    KUWAIT_CLASSIC_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="classic-selection"]').text
    assert KUWAIT_CLASSIC_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="classic-selection"]').click()
    time.sleep(5)

    KUWAIT_STC_PRICE_K = context.driver.find_element(By.XPATH, '//span[@id="vk-price"]')
    KUWAIT_STC_PRICE_VALUE = KUWAIT_STC_PRICE_K.text
    assert KUWAIT_STC_PRICE_VALUE == 'Starting: 2.50 KWD'
    time.sleep(2)

    KUWAIT_VISA_PRICE_K = context.driver.find_element(By.XPATH, '//span[@id="cc_kuw-price"]')
    KUWAIT_VISA_PRICE_VALUE = KUWAIT_VISA_PRICE_K.text
    assert KUWAIT_VISA_PRICE_VALUE == 'Starting: 9.60 USD'
    time.sleep(2)

    context.driver.get("https://subscribe.stctv.com/kw-en")
    time.sleep(5)

    PREMIUM_K = context.driver.find_element(By.XPATH, '//strong[@id="name-premium"]').text
    assert PREMIUM_K == 'PREMIUM'

    KUWAIT_PREMIUM_START_BUTTON = context.driver.find_element(By.XPATH, '//a[@id="premium-selection"]').text
    assert KUWAIT_PREMIUM_START_BUTTON == 'Start your trial'
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//a[@id="premium-selection"]').click()
    time.sleep(5)

    KUWAIT_STC_PRICE_P = context.driver.find_element(By.XPATH, '//span[@id="vk-price"]')
    KUWAIT_STC_PRICE_VALUE = KUWAIT_STC_PRICE_P.text
    assert KUWAIT_STC_PRICE_VALUE == 'Starting: 4.80 KWD'
    time.sleep(2)

    KUWAIT_VISA_PRICE_P = context.driver.find_element(By.XPATH, '//span[@id="cc_kuw-price"]')
    KUWAIT_VISA_PRICE_VALUE = KUWAIT_VISA_PRICE_P.text
    assert KUWAIT_VISA_PRICE_VALUE == 'Starting: 14.40 USD'
    time.sleep(2)








