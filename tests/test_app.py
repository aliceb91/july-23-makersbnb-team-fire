from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")

def test_get_list_all(page, test_web_address, db_connection):
    db_connection.seed('seeds/space.sql')
    page.goto(f"http://{test_web_address}/")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        'Name: test 1\nDescription: This is test 1\nPrice per Night: 10.0',
        'Name: test 2\nDescription: This is test 2\nPrice per Night: 20.0'
    ])

def test_get_user_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/space.sql')
    page.goto(f"http://{test_web_address}/users/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text('name 1')