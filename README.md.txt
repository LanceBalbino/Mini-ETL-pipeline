# Reddit :r/phinvest ETL Mini-Pipeline 

This code extracts posts and top-level comments from Reddit, transforms and stores them in multiple formats (CSV, JSON, SQLite), and prepares the data for downstream use.

## Features
- Extracts top posts from any subreddit
- Limits comments per post to avoid Reddit API overuse
- Saves data to CSV, JSON, and SQLite
- Clean structure: extract → transform → load

## Setup
1. Clone this repo
2. Create a `.env` file using the sample below:

CLIENT_ID=your_id
CLIENT_SECRET=your_secret
USER_AGENT=your_agent
USERNAME=your_username
PASSWORD=your_password

3. Install dependencies:
```bash
pip install -r requirements.txt

4. run the code.
I am using jupyterlab for this code, and I just created a new notebook and ran %run etl.py in the first cell
