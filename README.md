# Airport Navigation API Test
📌 Overview

Airport Navigation API Test adalah project API automation testing yang bertujuan untuk memverifikasi endpoint terkait data bandara dan navigasi penerbangan, seperti informasi airport, lokasi, dan validasi response API.

Project ini dibuat sebagai:
- Latihan & referensi API testing
- Contoh implementasi automation test untuk backend
- Portfolio QA (manual + automation)


## 🎯 Objectives

- Memastikan API airport navigation berjalan sesuai spesifikasi
- Memvalidasi response status, schema, dan data
- Menangkap bug lebih awal sebelum API digunakan oleh frontend / mobile apps
- Menyediakan dokumentasi test yang mudah dipahami

## 🧪 Scope of Testing

- Endpoint availability (health check)
- HTTP status code validation
- Response body & schema validation
- Data consistency (airport code, name, location, dll.)
- Negative testing (invalid parameter, empty value, dll.)

## 🛠️ Tech Stack
- Programming Language: Python
- Test Framework: Pytest
- Build Tool: -
- Assertion Library: Assertpy
- API Format: REST (JSON)

## 🧱 Project Architecture

```bash
airport-nav
 ┣ 📂src
 ┃ ┣ 📂test
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┣ 📂utils
 ┃ ┃ ┗ 📂data
 ┣ 📂config
 ┣ 📜pom.xml / package.json
 ┗ 📜README.md
```
Penjelasan

`api/` → test case per endpoint

`utils/` → helper (base request, config, auth)

`data/` → test data (json, payload, expected response)

`config/` → environment & base URL

---

## API Under Test (Example)
```json
GET /api/airports
GET /api/airports/{iata_code}
GET /api/airports?country=ID
```

## 🛠️ Setup

1. Clone repository
```bash
git clone https://github.com/rizkiamiftah/api-test.git
cd api-test/airport-nav
```
2. Install Python
```bash
https://www.python.org/downloads/
```
3. Install Pytest
```bash
pip install pytest
```
4. Install Dependencies
```bash
pip install assertpy
```

## ▶️ How to Run Tests
1) Run command to run all test cases
```python
pytest {folder_name}/
```
2) Using verbose for detail report
```python
pytest {folder_name}/ -v
```

## 🧾 Reports

Setelah eksekusi test, report akan tersedia di log terminal. Jika ingin lebih rapih bisa menggunakan library reporting seperti allure atau pytest report
```bash
https://pypi.org/project/pytest-md-report/
```

```bash
https://allurereport.org/docs/pytest/
```

## 👤 Author

- Rizkia Miftah — Lead QA
- Automation | Playwright | GitLab CI/CD | Test Strategy | Quality Leadership
🔗 LinkedIn: https://linkedin.com/in/rizkiamiftah
