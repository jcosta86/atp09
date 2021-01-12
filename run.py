from dotenv import load_dotenv
from frontend.web import app


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
    