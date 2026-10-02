from fastapi import FastAPI
import datetime
# These imports work if the files are in the same folder
from app.calculator import PAICalculator
from app.models import SessionLocal, DailyActivity, init_db

# THIS IS THE LINE THAT WAS MISSING
app = FastAPI()

# Initialize the database
init_db()
calc = PAICalculator()

@app.post("/garmin-webhook")
async def receive_garmin_data(data: dict):
    db = SessionLocal()
    
    # Calculate PAI
    score = calc.compute_daily_pai(data)
    
    # Save to Database
    new_entry = DailyActivity(
        subject_id=data.get('subject_id', 'unknown'),
        date=datetime.date.today(),
        steps=data.get('steps', 0),
        floors=data.get('floors', 0),
        intensity_mins=data.get('intensity_mins_weekly_avg', 0),
        pal=data.get('pal', 0.0),
        active_mins=data.get('active_mins', 0),
        pai_score=score
    )
    
    db.add(new_entry)
    db.commit()
    return {"status": "success", "calculated_pai": score}