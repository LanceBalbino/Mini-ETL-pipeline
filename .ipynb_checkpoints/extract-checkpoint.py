import praw
from config import REDDIT_CONFIG

# reddit = praw.Reddit(
#     client_id = "dHXyohqikVfnBajJZRAg_Q",
#     client_secret = "N8VpDkc_gkEhrrb7KcG04N_dxISDOg",
#     user_agent = "get_data",
#     username = "Snappy_spot",
#     password = "Hitharder_123"
# )

def get_reddit_client():
    return praw.Reddit(
        client_id = REDDIT_CONFIG["client_id"],
        client_secret = REDDIT_CONFIG["client_secret"],
        username = REDDIT_CONFIG["username"],
        password = REDDIT_CONFIG["password"],
        user_agent = REDDIT_CONFIG["user_agent"],
    )

# subreddit = reddit.subreddit("phinvest")
# for post in subreddit.top(time_filter = "all", limit = 10):
#     print(f"Title: {post.title}")
#     print(f"Score: {post.score}")
#     print(f"URL: {post.url}")
#     post.comments.replace_more(limit = 10)
#     for comment in post.comments.list():
#         print(comment.body)
#     print("-"*40)

def fetch_top_posts_with_comments(subreddit_name, post_limit = 10, comment_limit = 10):
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    data = []
    for idx, post in enumerate (subreddit.top(time_filter = "all", limit = post_limit), start = 1):
        
        print(f"Fetching post {idx}/{post_limit}: {post.title}")
        
        post.comments.replace_more(limit = 0)
        top_comments = post.comments[:comment_limit]
    
        comments_data = []
        
        for c in top_comments:
            comments_data.append({
                "comment_id" : c.id,
                "parent_id": c.parent_id,
                "body": c.body,
                "score": c.score
            })

        data.append({
            "post_id": post.id,
            "title": post.title,
            "body": post.selftext,
            "score": post.score,
            "url": post.url,
            "num_comments": post.num_comments,
            "comments": comments_data
        })

    print(f"finished. total posts fetched: {len(data)}")
    return data