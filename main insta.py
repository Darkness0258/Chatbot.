from instapydl import Reel

# Replace with your reel URL
url = "https://www.instagram.com/reel/DOGP5BKk587/"

reel = Reel(url)
metadata = reel.scrape_post()

print("Metadata:", metadata)

# (Optional) Download the reel video
reel.download("my_reel.mp4")
