from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from typing import List

app = FastAPI(title="ATS Analyzer API")

# ✅ Root route
@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

# ✅ CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Pydantic response model
class ATSResponse(BaseModel):
    score: int
    missing_keywords: List[str]
    suggestions: List[str]
    strengths: List[str]

# ✅ Main route
@app.post("/analyze", response_model=ATSResponse)
async def analyze_cv(file: UploadFile = File(...)):
    missing_keywords = [
        "Machine Learning",
        "Data Analysis",
        "Cloud Computing",
        "Project Management",
        "Customer Relations",
    ]
    suggestions = [
        "Include more quantifiable achievements with numbers and metrics",
        "Add industry-specific keywords like 'agile methodology' and 'project lifecycle'",
        "Use action verbs at the beginning of bullet points",
        "Include a professional summary at the top of your CV",
    ]
    strengths = [
        "Clear chronological work history",
        "Good use of industry terminology",
        "Relevant job titles match the target position",
        "Well-structured sections",
    ]
    score = random.randint(70, 85)
    return ATSResponse(
        score=score,
        missing_keywords=missing_keywords,
        suggestions=suggestions,
        strengths=strengths,
    )