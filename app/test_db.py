from sqlalchemy import text
from app.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT version(), current_database(), current_user")
        )
        print(result.fetchone())
        print("Database connection successful!")

except Exception as error:
    print("Database connection failed!")
    print(error)

finally:
    engine.dispose()