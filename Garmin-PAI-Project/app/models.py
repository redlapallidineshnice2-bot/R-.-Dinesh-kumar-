from sqlalchemy import Column, Integer, Float, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 1. Define the Base
Base = declarative_base()

# 2. Define the Table Model
class DailyActivity(Base):
    __tablename__ = 'daily_activities'
    
    id = Column(Integer, primary_key=True)
    subject_id = Column(String(50))
    date = Column(Date)
    steps = Column(Integer)
    floors = Column(Integer)
    intensity_mins = Column(Integer)
    pal = Column(Float)
    active_mins = Column(Integer)
    pai_score = Column(Float)

# 3. Setup Database Path (creates a 'data' folder inside 'app')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "data")
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

# 4. Create Engine and Session
DB_PATH = os.path.join(DB_DIR, "physical_activity.db")
engine = create_engine(f'sqlite:///{DB_PATH}', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Function to initialize database
def init_db():
    Base.metadata.create_all(bind=engine)