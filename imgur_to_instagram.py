import requests
import os

# Imgur API credentials
IMGUR_CLIENT_ID = os.getenv("IMGUR_CLIENT_ID")

# Instagram API credentials
MAKE_WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")  # Webhook URL from Make.com

def get_latest_imgur_url():
    """Fetch the latest uploaded image/video URL from Imgur."""
    headers = {"Authorization": f"Client-ID {IMGUR_CLIENT_ID}"}
    response = requests.get("https://api.imgur.com/3/account/me/images", headers=headers)
    data = response.json()
    
    if data["success"] and data["data"]:
        return data["data"][0]["link"]  # Get latest upload
    return None

def send_to_make(imgur_url):
    """Send the Imgur URL to Make.com for Instagram posting."""
    payload = {"imgur_url": imgur_url}
    response = requests.post(MAKE_WEBHOOK_URL, json=payload)
    print("Sent to Make.com:", response.status_code, response.text)

if __name__ == "__main__":
    latest_url = get_latest_imgur_url()
    if latest_url:
        send_to_make(latest_url)
