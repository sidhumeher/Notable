import asyncio
from pyppeteer import launch


async def main(searchTerm):
    browser = await launch(headless=False, autoClose = False)
    page = (await browser.pages())[0]

    await page.goto('https://data.gov')

    # await browser.close()
    
    # Enter search key
    await page.type('input[id=search-header]', searchTerm)
    await page.keyboard.press('Enter')
    
    
# Enter search key
def searchKeyword():
    searchKey = input("Enter search word:")
    #print(searchKey)
    return searchKey
    
    
searchKey = searchKeyword()
asyncio.get_event_loop().run_until_complete(main(searchKey))


    
