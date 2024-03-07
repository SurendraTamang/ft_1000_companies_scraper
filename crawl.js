const fs = require("fs");
const output = "data/js_ft1000-2024.html"
const url = "https://www.ft.com/ft1000-2024"
const response = fetch(url, {
  headers: {
    accept:
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "if-none-match": 'W/"f0511-teVvVL0GzelWnYO1DSwRrlRPiOs"',
    "sec-ch-ua":
      '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
  },
  referrerPolicy: "strict-origin-when-cross-origin",
  body: null,
  method: "GET",
})
  .then((response) => response.text())
  .then((text) => {
    // Save to html file
    fs.writeFileSync(output, text, "utf-8");
    console.log("File saved successfully!");
  })
  .catch((error) => {
    console.error("Error:", error);
  });
