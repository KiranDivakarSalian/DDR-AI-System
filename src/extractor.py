import re


AREAS = ["hall", "bedroom", "bathroom", "balcony", "terrace", "external wall"]


def detect_area(text):
    text_lower = text.lower()
    found = []
    for area in AREAS:
        if area in text_lower:
            found.append(area.title())
    return found


def extract_issues(text):
    text_lower = text.lower()
    issues = []

    if "dampness" in text_lower:
        issues.append("Dampness")

    if "efflorescence" in text_lower:
        issues.append("Efflorescence")

    if "crack" in text_lower:
        issues.append("Cracks")

    if "tile joint" in text_lower or "gaps" in text_lower:
        issues.append("Tile Joint Gaps")

    if "seepage" in text_lower:
        issues.append("Seepage")

    if "leakage" in text_lower:
        issues.append("Leakage")

    return list(set(issues))


def extract_thermal_data(text):
    hotspots = re.findall(r'Hotspot\s*:\s*(\d+\.?\d*)', text)
    coldspots = re.findall(r'Coldspot\s*:\s*(\d+\.?\d*)', text)

    hotspots = list(map(float, hotspots)) if hotspots else []
    coldspots = list(map(float, coldspots)) if coldspots else []

    return {
        "hotspots": hotspots,
        "coldspots": coldspots,
        "avg_hotspot": sum(hotspots) / len(hotspots) if hotspots else None,
        "avg_coldspot": sum(coldspots) / len(coldspots) if coldspots else None
    }