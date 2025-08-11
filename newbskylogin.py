import asyncio
import bsky_id_pw
from playwright.async_api import async_playwright

async def new_bsky_login():
    async with async_playwright() as bsky:
        browser = await bsky.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        async def wait(time):
            await page.wait_for_timeout(time)

        await page.goto("https://bsky.app")
        print('# bsky 이동')
        await wait(5000)

        # 블스 최초 로그인
        await page.goto("https://bsky.app/")
        await page.get_by_role("button", name="로그인").click()
        await page.get_by_test_id("loginUsernameInput").click()
        await page.get_by_test_id("loginUsernameInput").fill(bsky_id_pw.id)
        await page.get_by_test_id("loginUsernameInput").press("Tab")
        await page.get_by_test_id("loginPasswordInput").fill(bsky_id_pw.pw)
        await page.get_by_test_id("loginPasswordInput").press("Enter")
    #
        await wait(3000)
        print('# bsky login success')

        await context.storage_state(path="bsky_login_state.json")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(new_bsky_login())
