from app import create_app, db
from app.models import Category, Thread

app = create_app()

@app.cli.command("init-db")
def init_db():
    db.drop_all()
    db.create_all()
    print("✅ Database initialized")




if __name__ == "__main__":
    app.run(debug=True)
