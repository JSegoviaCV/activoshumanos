from playwright.sync_api import sync_playwright, Page, expect
import os

def verify_skip_link(page: Page):
    """
    Verifies that the 'skip to content' link is visually hidden by default,
    appears on keyboard focus, and navigates to the main content on activation.
    """
    # 1. Navigate to the local server URL.
    page.goto("http://localhost:8000")

    # 2. Verify the link is initially hidden (not visible on the viewport).
    skip_link = page.locator(".skip-link")
    expect(skip_link).not_to_be_in_viewport()

    # 3. Press 'Tab' to focus the link and make it visible.
    page.keyboard.press("Tab")

    # 4. Verify the link is now visible and has the correct styles.
    expect(skip_link).to_be_in_viewport()

    # 5. Take a screenshot of the focused link.
    os.makedirs("verification", exist_ok=True)
    page.screenshot(path="verification/focused_link_final.png")

    # 6. Activate the link.
    page.keyboard.press("Enter")

    # 7. Verify that the main content is now focused.
    main_content = page.locator("#main-content")
    expect(main_content).to_be_focused()

    # 8. Take a screenshot to confirm the page has scrolled.
    page.screenshot(path="verification/scrolled_to_content_final.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_skip_link(page)
            print("Verification script completed successfully.")
        finally:
            browser.close()
