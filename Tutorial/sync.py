from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.Google.com/")
    page.screenshot(path="screenshot/demo.png")
    browser.close()

