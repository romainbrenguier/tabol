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

   # Optional: Customize the model (defaults to gemini-3.5-flash)
   AI_MODEL=gemini-3.5-flash
   ```

5. **Access the Game**
   Open your browser and navigate to:
   [http://127.0.0.1:8000/api/chat/](http://127.0.0.1:8000/api/chat/)

## Deployment to Vercel

This app is configured for easy deployment on [Vercel](https://vercel.com/).

### Prerequisites

1.  A Vercel account.
2.  The [Vercel CLI](https://vercel.com/docs/cli) installed (optional but recommended).

### Steps to Deploy

1.  **Connect your Repository**
    Push your code to a GitHub, GitLab, or Bitbucket repository and import it into Vercel.

2.  **Configure Environment Variables**
    In your Vercel project settings, add the following Environment Variables:
    - `DJANGO_SECRET_KEY`: A long, random string for Django's security.
    - `DEBUG`: Set to `False` for production.
    - `GEMINI_API_KEY` (or `OPENAI_API_KEY`): Your AI provider's API key.
    - `AI_MODEL`: (Optional) e.g., `gemini-3.5-flash`.

3.  **Deployment**
    Vercel will automatically detect the `vercel.json` and `requirements.txt` files and deploy the application using the `@vercel/python` runtime.

### Note on Database
This project currently uses SQLite, which is file-based. On Vercel, the filesystem is ephemeral, meaning database changes will not persist between deployments or function cold starts. For production use, consider switching to a managed database like Postgres and updating the `DATABASES` setting in `tabol_project/settings.py`.
