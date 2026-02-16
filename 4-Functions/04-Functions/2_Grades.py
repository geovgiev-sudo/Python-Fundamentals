def grades(grade):
    if 2 <= grade < 3:
        return "Fail"
    elif 3 <= grade < 3.50:
        return "Poor"
    elif 3.50 <= grade < 4.50:
        return "Good"
    elif 4.50 <= grade < 5.50:
        return "Very Good"
    elif 5.50 <= grade <= 6:
        return "Excellent"
    return None

grade_received = float(input())
result = grades(grade_received)
print(result)

