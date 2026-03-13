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
`bash
git clone https://github.com/mainuddin-md/Django-projects.git
cd Django-projects
`

**2. Install dependencies**
`bash
pip install django djangorestframework djangorestframework-simplejwt
`

**3. Apply database migrations**
`bash
python manage.py makemigrations
python manage.py migrate
`

**4. Create a Superuser (Admin)**
*You will need this to edit/delete records and generate JWT tokens.*
`bash
python manage.py createsuperuser
`

**5. Run the development server**
`bash
python manage.py runserver
`

## 🌐 API Endpoints

Once the server is running, you can access the API at `http://127.0.0.1:8000/api/`.

### Authentication Endpoints
* `POST /api/token/` - Obtain JWT `access` and `refresh` tokens (requires username/password in body).
* `POST /api/token/refresh/` - Refresh an expired access token.

### Student CRUD Endpoints
* `GET /api/crud/` - List all students.
* `POST /api/crud/` - Add a new student (Requires JWT Bearer Token).
* `GET /api/crud/<id>/` - Retrieve a specific student.
* `PUT /api/crud/<id>/` - Update a specific student (Requires JWT Bearer Token).
* `DELETE /api/crud/<id>/` - Delete a specific student (Requires JWT Bearer Token).

## 👨‍💻 Author

**Mohammad Mainuddin**
