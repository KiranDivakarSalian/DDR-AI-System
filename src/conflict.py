def detect_conflicts(structured_data):
    conflicts = []

    for item in structured_data:
        issues = item["issues"]
        thermal = item["thermal"]

        if "No leakage" in issues and thermal["coldspot"] and thermal["coldspot"] < 22:
            conflicts.append({
                "area": item["area"],
                "message": "Inspection says no leakage, but thermal indicates moisture."
            })

    return conflicts