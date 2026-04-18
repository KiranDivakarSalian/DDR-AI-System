def deduplicate(data):
    merged = {}

    for item in data:
        area = item["area"]

        if area not in merged:
            merged[area] = item
        else:
            merged[area]["issues"] = list(
                set(merged[area]["issues"] + item["issues"])
            )
            merged[area]["images"].extend(item["images"])

    return list(merged.values())