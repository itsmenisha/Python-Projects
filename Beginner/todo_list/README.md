# Django To-Do List

A simple **To-Do List** application built using **Django**. This project helped me gain a deeper understanding of **Python**, Django's **frontend-backend connection**, and how web applications work. It was an **amazing and interactive** learning experience! I learned how to manage databases efficiently, structure a Django project properly, and handle both frontend and backend seamlessly. 

## Features  
- **Create, Read, Update, and Delete (CRUD) tasks** for daily task management.  
- **User authentication** to keep tasks private and secure.  
- **Django's templating system** for a clean and responsive UI.  
- **Database integration** using Django's ORM.  

## Installation & Setup  

### 1. Clone the repository
```
git clone https://github.com/itsmenisha/projects/Beginner/todolist.git
cd django-todolist
```

### 2. Create and activate a virtual environment
```
python -m venv venv  
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Apply database migrations
```
python manage.py migrate
```

### 5. Create a superuser (optional for admin access)
```
python manage.py createsuperuser
```

### 6. Run the development server
```
python manage.py runserver
```
Then open `http://127.0.0.1:8000/` in your browser.

## Future Improvements
As this was one of my **basic projects**, there are several things I would love to improve:
1. **Highlight busy days on the calendar** – Making days with tasks appear **darker** for better visibility.
2. **Enhanced UI/UX** – Improving the design and adding animations for a smoother experience.
3. **Task categorization** – Allow users to categorize tasks (e.g., Work, Personal, Urgent, etc.).
4. **Task reminders** – Add notification support to remind users of pending tasks.
5. **Drag & Drop task reordering** – Making it easier to manage and prioritize tasks.
6. **Start and end dates for tasks** – Implementing the ability to set start and end dates for tasks that require multiple days to complete.

