import json


def generate_ddr(structured_data, conflicts):
    report = {}

    # 1. Summary
    all_issues = []
    for item in structured_data:
        all_issues.extend(item["issues"])

    report["Property Issue Summary"] = list(set(all_issues))

    # 2. Area-wise Observations
    observations = []
    for item in structured_data:
        observations.append({
            "area": item["area"],
            "issues": item["issues"],
            "thermal": item["thermal"],
            "images": item["images"] if item["images"] else ["Image Not Available"]
        })

    report["Area-wise Observations"] = observations

    # 3. Root Cause
    report["Probable Root Cause"] = [
        "Water ingress through tile joints",
        "Capillary action",
        "Cracks in terrace and walls"
    ]

    # 4. Severity
    report["Severity Assessment"] = {
        "level": "High",
        "reason": "Multiple areas affected with moisture and structural risk"
    }

    # 5. Recommendations
    report["Recommended Actions"] = [
        "Grouting",
        "Waterproofing",
        "Crack sealing",
        "Plumbing repair"
    ]

    # 6. Additional Notes
    report["Additional Notes"] = conflicts if conflicts else ["No conflicts"]

    # 7. Missing Info
    report["Missing Information"] = [
        "Exact leakage timing: Not Available",
        "Plumbing confirmation: Not Available"
    ]

    return report


def save_json(report, path):
    with open(path, "w") as f:
        json.dump(report, f, indent=4)