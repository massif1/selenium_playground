from selenium import webdriver

firefox_browser = webdriver.Firefox()

firefox_browser.maximize_window()
firefox_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


def post_message():
    my_text = 'Calm down Satan'
    message_text = firefox_browser.find_element_by_id('user-message')
    message_text.click()
    message_text.send_keys(my_text)

    input_btn = firefox_browser.find_element_by_class_name('btn-default')
    input_btn.click()
    message_label = firefox_browser.find_element_by_id('display')

    if message_label.text == my_text:
        firefox_browser.quit()
        return print('bam')
    else:
        firefox_browser.quit()
        return print('baddong')


post_message()
