import asyncio
from playwright.async_api import async_playwright

async def bsky_login_session():
    async with async_playwright() as bsky:
        browser = await bsky.chromium.launch(headless=False)
        context = await browser.new_context(storage_state='bsky_login_state.json')
        page = await context.new_page()

        async def wait(time):
            await page.wait_for_timeout(time)

        # 블스 이동
        await page.goto("https://bsky.app")
        await wait(5000)

        while True:

            bsky_text = input("bsky: ")
            if bsky_text == "*":
                print('# finishing bsky')
                break

            await page.get_by_test_id("followingFeedPage").get_by_test_id("composeFAB").click()
            await wait(100)
            await page.get_by_role("textbox", name="Rich-Text Editor").click()
            await page.get_by_role("textbox", name="Rich-Text Editor").fill(bsky_text)
            await page.get_by_test_id("composerPublishBtn").click()

            await wait(2000)

asyncio.run(bsky_login_session())


