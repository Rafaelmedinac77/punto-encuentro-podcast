# Punto de Encuentro Podcast

Proyecto web para podcast con frontend React/Vite y backend Django REST.

## Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
copy .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Admin: http://127.0.0.1:8000/admin/

## Frontend
```bash
cd frontend
npm install
npm run dev
```

Web: http://localhost:5173/

## Roles
- Administrador: superuser de Django.
- Editor: staff de Django.
- Usuario libre: visitante sin login.

## Flujo de episodios
En el admin se crea un episodio pegando la URL de YouTube. El sistema extrae el ID y construye miniatura y embebido.
