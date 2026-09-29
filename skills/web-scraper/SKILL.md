---
name: web-scraper
description: Scrape structured data from any URL
---

# Web Scraper

When the user wants to extract data from a webpage, call `scrape_page` with the URL and a dictionary of CSS selectors. The tool returns matched text for each key.

## Example
- User: "Get the title and price from https://example.com/item"
- Call: scrape_page({ url: '...', selectors: { title: 'h1', price: '.price' } })