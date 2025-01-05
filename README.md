# Persian Blog Platform
This project is a **Persian-language blog** platform that allows users to create, manage, and interact with blog posts. It includes features for posting, commenting, account management, and user interaction with administrators through tickets. The blog is designed with several security and moderation tools to ensure a clean and safe environment.

## Features
- **Create Blog Posts**: Users can create blog posts, including text and images.
- **Comment System**: Users can comment on blog posts, but all posts and comments must be approved by the admin before being publicly visible.
- **Automatic Bad Word Filter**: Posts are automatically scanned for inappropriate language, and offending words are filtered out.
- **Admin Panel**: An admin panel is provided where administrators can approve or reject posts and comments.
- **Account Management**: - Create and delete accounts. - User login and password reset functionalities. - Edit user profile.
- **Post Management**: - Posts can be sorted by date or number of comments. - Search functionality based on posts and usernames.
- **Ticket System**: Users can submit tickets to the admin for queries or issues.

## Technologies Used
- **Backend**: [Django] - A Python web framework.
- **Frontend**: HTML, CSS, JavaScript.
- **Database**: SQLite (can be changed to PostgreSQL or MySQL as needed).
- **Authentication**: Custom authentication system for user management, login, and password reset.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ashkanhajian/your-repo.git
   cd your-repo
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
