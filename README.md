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

## Project Structure

```
├── .github/
│   └── workflows/
│       └──ci.yml
├── pages/                  # Page Object Model
│   ├── login_page.py
│   └── inventory_page.py
├── tests/                  # Test suite
│   ├── test_login.py
│   └── test_inventory.py
├── conftest.py             # Pytest fixtures
├──.gitignore
└──requirements.txt
```

## Test Coverage
- Login valid
- Login invalid
- Login with empty credentials
- Inventory page loaded
- Count products
- Add to cart

## Run locally

```bash
# Install dependencies
pip install -r requirements.txt

# Install Chromium
playwright install chromium

# Run all tests
pytest -v

# Run headed with slow motion (useful for debugging)
pytest -v --headed --slowmo 500
```

## CI/CD

The project includes a GitHub Actions pipeline configured to run on every push and pull request to `main`.

## Docker

The project is fully containerized and can be run without any local Python or Playwright setup.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

### Build the image

```bash
docker build -t sauce-ui-tests .
```

### Run the tests

```bash
docker run sauce-ui-tests
```