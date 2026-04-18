from sqlalchemy.orm import Session
from .models import Activity, Participant

def seed_activities(db: Session):
    # Only seed if no activities exist
    if db.query(Activity).count() > 0:
        return
    activities = [
        Activity(
            name="Chess Club",
            description="Learn strategies and compete in chess tournaments",
            schedule="Fridays, 3:30 PM - 5:00 PM",
            max_participants=12,
            participants=[Participant(email="michael@mergington.edu"), Participant(email="daniel@mergington.edu")]
        ),
        Activity(
            name="Programming Class",
            description="Learn programming fundamentals and build software projects",
            schedule="Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            max_participants=20,
            participants=[Participant(email="emma@mergington.edu"), Participant(email="sophia@mergington.edu")]
        ),
        Activity(
            name="Gym Class",
            description="Physical education and sports activities",
            schedule="Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            max_participants=30,
            participants=[Participant(email="john@mergington.edu"), Participant(email="olivia@mergington.edu")]
        ),
        Activity(
            name="Soccer Team",
            description="Join the school soccer team and compete in matches",
            schedule="Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            max_participants=22,
            participants=[Participant(email="liam@mergington.edu"), Participant(email="noah@mergington.edu")]
        ),
        Activity(
            name="Basketball Team",
            description="Practice and play basketball with the school team",
            schedule="Wednesdays and Fridays, 3:30 PM - 5:00 PM",
            max_participants=15,
            participants=[Participant(email="ava@mergington.edu"), Participant(email="mia@mergington.edu")]
        ),
        Activity(
            name="Art Club",
            description="Explore your creativity through painting and drawing",
            schedule="Thursdays, 3:30 PM - 5:00 PM",
            max_participants=15,
            participants=[Participant(email="amelia@mergington.edu"), Participant(email="harper@mergington.edu")]
        ),
        Activity(
            name="Drama Club",
            description="Act, direct, and produce plays and performances",
            schedule="Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            max_participants=20,
            participants=[Participant(email="ella@mergington.edu"), Participant(email="scarlett@mergington.edu")]
        ),
        Activity(
            name="Math Club",
            description="Solve challenging problems and participate in math competitions",
            schedule="Tuesdays, 3:30 PM - 4:30 PM",
            max_participants=10,
            participants=[Participant(email="james@mergington.edu"), Participant(email="benjamin@mergington.edu")]
        ),
        Activity(
            name="Debate Team",
            description="Develop public speaking and argumentation skills",
            schedule="Fridays, 4:00 PM - 5:30 PM",
            max_participants=12,
            participants=[Participant(email="charlotte@mergington.edu"), Participant(email="henry@mergington.edu")]
        ),
    ]
    db.add_all(activities)
    db.commit()
