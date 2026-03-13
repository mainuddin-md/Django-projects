# Django Student Management System & REST API

A full-stack CRUD (Create, Read, Update, Delete) application built with Django. This project features a dual-interface design: a traditional browser-based frontend using HTML templates and a fully functional REST API secured with JSON Web Tokens (JWT).

## 🚀 Features

* **Dual Interface:** Manage student records via a user-friendly web interface or programmatically via the REST API.
* **Role-Based Access Control (Frontend):** * Public users can view and add student records.
  * Only authenticated Admin/Superusers can edit or delete records.
* **JWT Authentication (API):** The REST API is secured using `djangorestframework-simplejwt`. Endpoints are protected to ensure only authenticated users can modify data.
* **Browsable API:** Includes Django Rest Framework's built-in UI for easy API testing and interaction.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **API Framework:** Django REST Framework (DRF)
* **Authentication:** Built-in Session Auth (Frontend) & SimpleJWT (API)
* **Frontend:** HTML, Bootstrap (for styling), Django Forms

## ⚙️ Installation and Setup

Follow these steps to get the project running on your local machine.

**1. Clone the repository**
```bash
git clone [https://github.com/mainuddin-md/Django-projects.git](https://github.com/mainuddin-md/Django-projects.git)
cd Django-projects
# Navigate into your specific project folder (e.g., crudproject1)
