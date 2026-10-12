from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to CareerPath AI!",
        "status": "Backend is working"
    })

@app.route("/generate-roadmap", methods=["POST"])
def generate_roadmap():
    data = request.get_json() or {}

    education = data.get("education", "Not provided")
    career = data.get("career", "Unknown Career")
    skill_level = data.get("skill_level", "Beginner")
    study_hours = data.get("study_hours", "Not provided")

    roadmaps = {
        "AI Engineer": [
            "Phase 1: Learn Python fundamentals",
            "Phase 2: Learn NumPy and Pandas",
            "Phase 3: Study mathematics and statistics",
            "Phase 4: Learn machine learning",
            "Phase 5: Learn deep learning",
            "Phase 6: Build AI projects"
        ],
        "Web Developer": [
            "Phase 1: Learn HTML",
            "Phase 2: Learn CSS",
            "Phase 3: Learn JavaScript",
            "Phase 4: Learn a frontend framework",
            "Phase 5: Learn backend development",
            "Phase 6: Build and deploy websites"
        ],
        "Python Developer": [
            "Phase 1: Learn Python fundamentals",
            "Phase 2: Practice functions and data structures",
            "Phase 3: Learn object-oriented programming",
            "Phase 4: Learn databases and APIs",
            "Phase 5: Build Python applications",
            "Phase 6: Learn testing and deployment"
        ],
        "Data Analyst": [
            "Phase 1: Learn Python fundamentals",
            "Phase 2: Learn Excel and SQL",
            "Phase 3: Learn NumPy and Pandas",
            "Phase 4: Learn data visualization",
            "Phase 5: Practice statistics",
            "Phase 6: Build data analysis projects"
        ],
        "Data Scientist": [
            "Phase 1: Learn Python fundamentals",
            "Phase 2: Study statistics and probability",
            "Phase 3: Learn NumPy and Pandas",
            "Phase 4: Learn machine learning",
            "Phase 5: Practice data visualization",
            "Phase 6: Build data science projects"
        ]
    }

    roadmap = roadmaps.get(
        career,
        ["Start by learning programming fundamentals"]
    )

    return jsonify({
        "education": education,
        "career": career,
        "skill_level": skill_level,
        "study_hours": study_hours,
        "roadmap": roadmap,
        "message": f"Python generated your {career} roadmap!"
    })

if __name__ == "__main__":
    app.run(debug=True)
    