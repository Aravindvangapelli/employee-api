from app.core.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password

db = SessionLocal()

user = User(
    emailid="admin@gmail.com",
    password=hash_password("admin123")
)

db.add(user)
db.commit()

print("User Created Successfully")