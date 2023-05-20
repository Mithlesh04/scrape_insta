const {Builder} = require('selenium-webdriver');

(async function example() {
  let driver = await new Builder().forBrowser('firefox').build();
  try {
    await driver.get('https://www.instagram.com/monikamanchanda/?hl=en');
  } finally {

    driver.executeScript(()=>window._sharedData.entry_data.ProfilePage[0]).then(d=>{
      console.log('excute = ',d)
      driver.quit()
    })

  }
})();