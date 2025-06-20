def flatten_data(raw_data):
    post_rows = []
    comment_rows = []

    for item in raw_data:
        post_rows.append({
            "post_id": item["post_id"],
            "title": item["title"],
            "body": item["body"],
            "score": item["score"],
            "url": item["url"],
            "num_comments": item["num_comments"]
        })

        for c in item["comments"]:
            comment_rows.append({
                "comment_id": c["comment_id"],
                "post_id": item["post_id"],
                "parent_id": c["parent_id"],
                "body": c["body"],
                "score": c["score"]
            })

    return post_rows, comment_rows