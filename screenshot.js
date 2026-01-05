const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto('http://localhost:8000');
  await page.screenshot({ path: 'mobile_screenshot.png' });
  await browser.close();
})();
