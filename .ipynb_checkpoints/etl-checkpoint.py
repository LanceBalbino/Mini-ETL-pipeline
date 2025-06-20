from extract import fetch_top_posts_with_comments
from transform import flatten_data
from load import save_to_csv, save_to_json, save_to_sqlite

def run():
    data = fetch_top_posts_with_comments("phinvest", post_limit = 55, comment_limit = 30) 
    posts, comments = flatten_data(data)

    save_to_csv(posts,comments)
    save_to_json(data)
    save_to_sqlite(posts,comments)
    print("ETL complete, data saved")

if __name__ == "__main__":
    run()

