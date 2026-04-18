

from app import SessionLocal
from seed import seed_activities

def main():
    db = SessionLocal()
    seed_activities(db)
    db.close()

if __name__ == "__main__":
    main()
