# Personal Portfolio

A Django personal portfolio with a private, admin-only dashboard for managing projects and tech stacks. Projects added through the dashboard show up on the public portfolio automatically.

- **Live site:** https://gabriellelansangan.pythonanywhere.com
- **Admin sign-in (live):** https://gabriellelansangan.pythonanywhere.com/login/

## Features

- Public portfolio page that renders projects, skills, and profile information from the database
- Project detail pages, a contact/inquiry page, and a testimonials page
- **Admin-only sign-in** at `/login/`: only superusers can authenticate, and regular accounts are rejected even if they exist
- **Dashboard** at `/dashboard/` with two table views:
  - Projects: name, description (truncated to 50 characters), tech stacks (comma separated), and a clickable link
  - Tech stacks: name, projects it was used in, and the date it was added
- **Create views** for projects and tech stacks with required-field validation
- A single tech stack (for example, Python) can be linked to many projects without duplicates

## Tech Stack

- Python and Django
- SQLite (default Django database)
- Bootstrap 5 and custom CSS
- python-decouple for environment variables
- Deployed on PythonAnywhere

## Requirements

- Python 3.12 or newer
- Git

## Local Setup

Follow these steps in order. They assume a fresh clone. No database file or virtual environment is included in the repository, so you create both yourself.

1. **Clone the repository**

   ```bash
   git clone https://github.com/gabriellelansangan/OBJORPROG2026.git
   cd OBJORPROG2026
   ```

2. **Create and activate a virtual environment**

   macOS / Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Windows:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Move into the folder that contains `manage.py`**

   ```bash
   cd myproject
   ```

   Run every `python manage.py ...` command below from this folder.

5. **Create your environment file**

   macOS / Linux:

   ```bash
   cp ../.env.example .env
   ```

   Windows:

   ```bash
   copy ..\.env.example .env
   ```

   Open `.env` and replace the placeholder `SECRET_KEY` with your own. You can generate one with:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
   ```

6. **Run the migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create an admin (superuser) account**

   ```bash
   python manage.py createsuperuser
   ```

   Enter a username, email (optional), and password when prompted. You will use this account to sign in to the dashboard.

8. **Start the development server**

   ```bash
   python manage.py runserver
   ```

9. Open http://127.0.0.1:8000/ in your browser.

## Environment Variables

All variables live in a `.env` file next to `manage.py`. The `.env` file is ignored by Git. Use `.env.example` as the template.

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key | a long random string |
| `DEBUG` | Debug mode | `True` locally, `False` in production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `localhost,127.0.0.1` |

## Admin Access (Login Instructions)

The admin dashboard is not linked from the public portfolio. Reach it with these steps:

1. Make sure you have created a superuser (see Local Setup, step 7).
2. Go to the sign-in page:
   - Local: http://127.0.0.1:8000/login/
   - Live: https://gabriellelansangan.pythonanywhere.com/login/
3. Sign in with your **superuser** username and password.
4. After a successful sign-in you are redirected to `/dashboard/`.

Notes:

- Only superuser accounts can sign in. A regular user account is rejected with an "administrators only" message, even with the correct password.
- Visiting `/dashboard/` or any create page while signed out redirects to `/login/`.
- Use **Sign out** in the dashboard navigation bar to log out.

## Using the Dashboard

1. **Add tech stacks first.** Open **Tech Stacks**, click the create button, enter a name (for example, `Python`), and save. Names must be unique.
2. **Add a project.** Open **Projects**, click the create button, then fill in the project name, description, tech stack (radio buttons listing every tech stack you created), and link. All fields are required, and the form shows errors if anything is missing or invalid.
3. **Check the result.** The new project appears in the Projects table and on the public portfolio page (`/`).

## Project Structure

```
OBJORPROG2026/
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── core/               # Main app
│   ├── models.py       # Project, TechStack, and other models
│   ├── views.py        # Public pages and dashboard views
│   ├── forms.py        # Admin login form and create forms
│   ├── urls.py
│   ├── templates/
│   │   ├── index.html  # Public portfolio
│   │   └── dashboard/  # Admin sign-in, tables, and create forms
│   └── static/
└── myproject/          # Django project (settings, root URLs, manage.py)
```

## Deployment (PythonAnywhere)

These are the steps used for the live site. Replace `gabriellelansangan` with your own PythonAnywhere username if you deploy your own copy.

1. Push the code to GitHub and merge it into `main` through a pull request.
2. In a PythonAnywhere **Bash console**, clone the repository:

   ```bash
   git clone https://github.com/gabriellelansangan/OBJORPROG2026.git
   cd OBJORPROG2026
   ```

3. Create a virtual environment and install the dependencies. Use a Python version that PythonAnywhere offers and that meets the requirements above (check with `ls /usr/bin/python3*`):

   ```bash
   python3.12 -m venv ~/.virtualenvs/portfolio-env
   source ~/.virtualenvs/portfolio-env/bin/activate
   pip install -r requirements.txt
   ```

4. Move into the folder that contains `manage.py` and create the environment file:

   ```bash
   cd myproject
   cp ../.env.example .env
   nano .env
   ```

   Set a new `SECRET_KEY`, `DEBUG=False`, and `ALLOWED_HOSTS=gabriellelansangan.pythonanywhere.com`.

5. Set up the database, admin account, and static files:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic
   ```

   `collectstatic` ends with a line naming the folder it copied the files to. Note that path for the next step.

6. On the **Web** tab, add a new web app with **Manual configuration**, then set:
   - **Source code:** `/home/gabriellelansangan/OBJORPROG2026/myproject`
   - **Virtualenv:** `/home/gabriellelansangan/.virtualenvs/portfolio-env`
   - **Static files:** URL `/static/` pointing to the folder printed by `collectstatic`
7. Open the WSGI configuration file from the Web tab, replace its contents with the following, and save:

   ```python
   import os
   import sys

   for path in ['/home/gabriellelansangan/OBJORPROG2026',
                '/home/gabriellelansangan/OBJORPROG2026/myproject']:
       if path not in sys.path:
           sys.path.insert(0, path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

8. Click **Reload** on the Web tab and visit the site.

### Updating the live site

```bash
cd ~/OBJORPROG2026
git pull
cd myproject
source ~/.virtualenvs/portfolio-env/bin/activate
python manage.py migrate
python manage.py collectstatic
```

Then click **Reload** on the Web tab.

### Troubleshooting

- **"Something went wrong" page:** open the **Error log** link on the Web tab and read the last lines.
- **`DisallowedHost`:** `ALLOWED_HOSTS` in the server's `.env` must match the site URL exactly.
- **`SECRET_KEY not found`:** the `.env` file is missing or is not next to `manage.py`.
- **Images or styling missing:** check the Static files mapping on the Web tab and run `collectstatic` again.

## Author

Anna Gabrielle Lansangan