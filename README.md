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

4. **Configure AI (Optional but Recommended)**
   The game includes an AI bot that guesses the words you describe. To enable it, create a `.env` file in the root directory:
   ```env
   # Set your Gemini API key (or OPENAI_API_KEY)
   GEMINI_API_KEY=your_api_key_here

   # Optional: Customize the model (defaults to google/gemini-3.5-flash)
   AI_MODEL=google/gemini-3.5-flash
   ```

5. **Access the Game**
   Open your browser and navigate to:
   [http://127.0.0.1:8000/api/chat/](http://127.0.0.1:8000/api/chat/)
