def calculate_score(answers):
    scores = {
        "Technology & IT": 0,
        "Healthcare & Medicine": 0,
        "Business & Finance": 0,
        "Fashion & Styling": 0,
        "Government & Public Service": 0
    }

    if answers.get("subject") == "cs":
        scores["Technology & IT"] += 40

    if answers.get("subject") == "bio":
        scores["Healthcare & Medicine"] += 40

    if answers.get("subject") == "commerce":
        scores["Business & Finance"] += 40

    if answers.get("subject") == "arts":
        scores["Fashion & Styling"] += 40

    return scores