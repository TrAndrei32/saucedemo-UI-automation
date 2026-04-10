# SauceDemo UI Automation

![CI](https://github.com/TrAndrei32/saucedemo-UI-automation/actions/workflows/ci.yml/badge.svg)

## Description
UI test automation project for SauceDemo using Playwright and pytest, with CI/CD pipeline via GitHub Actions.

## Tech Stack
- Python
- Playwright
- pytest
- pytest html
- GitHub Actions

## Test Coverage
- Login valid
- Login invalid
- Login with empty credentials
- Inventory page loaded
- Count products
- Add to cart

## Run locally
```
pip install -r requirements.txt
playwright install chromium
pytest -v
```