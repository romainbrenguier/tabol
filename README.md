# tabol
A simple Javascript game with a Django backend for chat.

## How to run the app

1. **Install Dependencies**
   Ensure you have `uv` installed, then run:
   ```bash
   uv sync
   ```

2. **Setup Database**
   Run the migrations to create the database schema:
   ```bash
   uv run manage.py migrate
   ```

3. **Start the Server**
   Launch the Django development server:
   ```bash
   uv run manage.py runserver
   ```

4. **Access the Game**
   Open your browser and navigate to:
   [http://127.0.0.1:8000/api/chat/](http://127.0.0.1:8000/api/chat/)
