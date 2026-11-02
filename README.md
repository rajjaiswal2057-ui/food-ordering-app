# Online Food Ordering Application

![CI](https://github.com/rajjaiswal2057-ui/food-ordering-app/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Docker](https://img.shields.io/badge/docker-ready-2496ED)
![Tests](https://img.shields.io/badge/tests-17%20passed-brightgreen)

A lightweight Python application for an online food ordering system, built to demonstrate a complete DevOps lifecycle: version control with Git, CI/CD with GitHub Actions, containerization with Docker and automated testing with Pytest.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Getting Started](#getting-started)
- [Docker](#docker)
- [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Git Workflow](#git-workflow)
- [Author](#author)

## Features
- Menu browsing through a simple JSON API
- Cart management with validation (unknown items and non-positive quantities are rejected)
- Order total calculation with a percentage discount (0-100%)
- Parameterized automated test suite (17 tests)
- Containerized with Docker (port mapping 8080 to 5000)
- Automated CI with GitHub Actions on every push to main

## Architecture

### Delivery pipeline

```mermaid
flowchart LR
    Dev["Developer"] --> Feature["feature/cart branch"]
    Feature -->|merge| Main["main branch"]
    Main -->|git push| GH["GitHub repository"]
    GH -->|triggers| CI["GitHub Actions CI"]
    CI --> T1["Run calculate_total.py"]
    CI --> T2["Run pytest"]
    Main -->|docker build| Image["Docker image"]
    Image -->|"docker run -p 8080:5000"| Container["food-app container"]
    Client["Browser or curl"] -->|HTTP| Container
```

### Application modules

```mermaid
flowchart TD
    app["app.py - HTTP server on port 5000"] --> menu["menu.py - menu data"]
    cart["cart.py - add_to_cart"] --> menu
    calc["calculate_total.py - sample order"] --> cart
    calc --> menu
    order["order.py - calculate_order_total"]
    tests["test_order.py - pytest suite"] --> order
```

## Testing

```bash
pip install pytest
pytest -v
```

`calculate_order_total(subtotal, discount_percent=0)` returns the total after applying a percentage discount, rounded to 2 decimals. It raises `ValueError` for a negative subtotal or a discount outside 0-100, and `TypeError` for a non-numeric subtotal.

| Category | Examples covered |
|----------|------------------|
| Normal inputs | 100 with 10% discount = 90.0 |
| Zero values | subtotal 0, discount 0 |
| Invalid inputs | negative subtotal, discount above 100, non-numeric subtotal |
| Discount boundaries | 0%, 100%, 0.01%, 99.99% |

All tests are parameterized with `pytest.mark.parametrize` (17 test cases in total).

## CI/CD Pipeline

The workflow in `.github/workflows/ci.yml` runs on every push to `main`:

| Step | Action |
|------|--------|
| 1 | Checkout code (`actions/checkout`) |
| 2 | Set up Python 3.12 (`actions/setup-python`) |
| 3 | Run `python calculate_total.py` |
| 4 | Run `pytest -v` |

The result is visible in the repository **Actions** tab.

## Git Workflow

- New work is developed on a feature branch (for example `feature/cart`).
- The branch is merged into `main` with a merge commit.
- A push to `main` triggers the CI pipeline.

## Author

**Raj Jaiswal** - [@rajjaiswal2057-ui](https://github.com/rajjaiswal2057-ui)
