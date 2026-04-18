def build_structure(text_data, image_data, thermal_data):
    structured = []

    for page in text_data:
        text = page["text"]

        from src.extractor import detect_area, extract_issues
        areas = detect_area(text)
        issues = extract_issues(text)

        for area in areas:
            structured.append({
                "area": area,
                "issues": issues,
                "thermal": {
                    "hotspot": thermal_data.get("avg_hotspot"),
                    "coldspot": thermal_data.get("avg_coldspot")
                },
                "images": [
                    img["path"] for img in image_data if img["page"] == page["page"]
                ]
            })

    return structured