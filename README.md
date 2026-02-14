# Django E-commerce API

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/django-5.0-green.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-14+-blue.svg)
![Stripe](https://img.shields.io/badge/stripe-integrated-blueviolet.svg)

A production-ready E-commerce REST API backend built with Django REST Framework (DRF), featuring secure payment processing via Stripe and automated product synchronization with Printify.

## 🚀 Key Features

*   **Robust Payment Integration**: Secure payment processing flows implemented with Stripe.
*   **Prooduct Synchronization**: Automated product retrieval and sync from Printify API.
*   **Granular Permissions**: Custom permission classes ensuring secure access control.
*   **Database**: Production-grade PostgreSQL integration.
*   **Authentication**: Token-based authentication (dj-rest-auth & allauth).
*   **Environment Configuration**: secure management of secrets via `.env`.

## 🛠️ Technology Stack

*   **Framework**: Django 5.0, Django REST Framework 3.15
*   **Database**: PostgreSQL
*   **Payment**: Stripe API
*   **3rd Party Integration**: Printify
*   **Utilities**: `django-environ`, `dj-rest-auth`, `django-allauth`

## ⚙️ Getting Started

### Prerequisites

*   Python 3.10+
*   PostgreSQL
*   Stripe & Printify Accounts (for API keys)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/lektronik/drf-ecommerce-api.git
    cd drf-ecommerce-api
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**
    Copy the example environment file and configure your keys.
    ```bash
    cp .env.example .env
    ```
    *Update `.env` with your Database credentials, Stripe keys, and Printify API token.*

5.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Run Server**
    ```bash
    python manage.py runserver
    ```

## 🔐 Environment Variables

Ensure the following variables are set in your `.env` file:

| Variable | Description |
| :--- | :--- |
| `SECRET_KEY` | Django Secret Key |
| `DEBUG` | Set to `True` for dev, `False` for prod |
| `db_NAME` | Database Name |
| `DB_USER` | Database User (default: postgres) |
| `DB_PASSWORD` | Database Password |
| `STRIPE_SECRET_KEY` | Stripe Secret Key |
| `PRINTIFY_API_KEY` | Printify API Token |

## 🧩 API Endpoints Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/products/` | List all products |
| `POST` | `/api/cart/` | Add item to cart |
| `POST` | `/api/orders/` | Create a new order |
| `POST` | `/api/auth/login/` | User login |

