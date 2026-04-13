from fastapi import FastAPI

app = FastAPI()

# This is the "mock" data we will use to calculate the average
moods = [
    {"score": 8, "note": "Great day at AGH!"},
    {"score": 5, "note": "A bit tired from labs"},
    {"score": 7, "note": "Finally finished the Git task"}
]

@app.get("/")
def read_root():
    return {"message": "Mood Tracking API Practice"}

@app.get("/moods/average")
def get_average_mood():
    if not moods:
        return {"average": 0}
    
    total_score = sum(m["score"] for m in moods)
    average = total_score / len(moods)
    
    return {"average": round(average, 2)}
