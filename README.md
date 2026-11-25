# ⚡ ChargeFuel — On-Demand Mobile Refueling & EV Charging Platform

<p align="left">
  <a href="https://github.com/Adiii-12/ChargeFuel">
    <img src="https://img.shields.io/badge/Repository-ChargeFuel-1F6FEB?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Repo" />
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  </a>
  <a href="https://git-scm.com/">
    <img src="https://img.shields.io/badge/VCS-Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  </a>
</p>

<p align="left">
  Welcome to <strong>ChargeFuel</strong>, a Django-powered web application built for on-demand mobile fuel delivery and EV charging assistance. Designed to help stranded or low-battery drivers request fuel or charging support with clear workflows, structured templates, and static media assets.
</p>

---

## 🛠️ Tech Stack & Languages Used

<p align="left">
  <a href="https://www.python.org/">
    <img src="https://skillicons.dev/icons?i=py" width="48" height="48" alt="Python" title="Python" />
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://skillicons.dev/icons?i=django" width="48" height="48" alt="Django" title="Django" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">
    <img src="https://skillicons.dev/icons?i=html" width="48" height="48" alt="HTML5" title="HTML5" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">
    <img src="https://skillicons.dev/icons?i=css" width="48" height="48" alt="CSS3" title="CSS3" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">
    <img src="https://skillicons.dev/icons?i=js" width="48" height="48" alt="JavaScript" title="JavaScript" />
  </a>
  <a href="https://www.sqlite.org/">
    <img src="https://skillicons.dev/icons?i=sqlite" width="48" height="48" alt="SQLite" title="SQLite" />
  </a>
  <a href="https://git-scm.com/">
    <img src="https://skillicons.dev/icons?i=git" width="48" height="48" alt="Git" title="Git" />
  </a>
  <a href="https://github.com/">
    <img src="https://skillicons.dev/icons?i=github" width="48" height="48" alt="GitHub" title="GitHub" />
  </a>
</p>

* **Python & Django** — Handles URL routing, view logic, ORM models, forms, and server-side rendering.
* **HTML5 & CSS3** — Structures application pages, layouts, and visual styling across templates and static assets.
* **JavaScript** — Adds interactive client-side behavior and dynamic UI updates.
* **SQLite** — Provides local relational database storage and schema migrations via Django ORM.
* **Git & GitHub** — Tracks source history, commits, and remote hosting at `https://github.com/Adiii-12/ChargeFuel.git`.
* **PyCharm & PowerShell** — Used for local development, `venv` virtual environment management, and Git operations.

---

## ✨ Features Included

* **Dual Service Focus (Fuel & EV Charging):** Supports requests and workflows for mobile fuel delivery and electric vehicle charging assistance.
* **Structured Django Architecture:** Separates routing (`urls.py`), request handlers (`views.py`), data models (`models.py`), HTML templates, and static assets (`development/static`).
* **Clean Dependency & Environment Setup:** Keeps local `venv` isolated via `.gitignore` while tracking dependencies in `requirements.txt`.
* **Rich Static Media Support:** Includes dedicated static assets and visual media under `development/static`.

---

## 🔄 System Flow & Process Diagrams

### 1. End-to-End Request & Service Flow

```mermaid
flowchart TD
    A["🚗 Driver / User"] --> B["🌐 Browser / Frontend UI (HTML, CSS, JS)"]
    B --> C["⚙️ Django URL Dispatcher (urls.py)"]
    C --> D["🧠 Django Views & Business Logic (views.py)"]
    D --> E{"Service Type?"}
    E -->|Mobile Fuel Delivery| F["⛽ Fuel Delivery Request & Dispatch"]
    E -->|EV Charging Support| G["🔋 EV Charging Request & Dispatch"]
    D <--> H[("🗄️ Django ORM / SQLite Database")]
    F --> H
    G --> H
    D --> I["📄 HTML Templates + 📁 Static Assets (development/static)"]
    I --> B
    B --> A

Author: Aditya Pratap Singh Sisodiya (Adiii-12)
