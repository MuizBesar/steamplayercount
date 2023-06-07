import requests
import tkinter as tk

# Steam Web API URL for retrieving player count
API_URL = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"

# Function to retrieve and update the player count
def update_player_count():
    try:
        # Send GET request to the Steam Web API
        response = requests.get(API_URL, params={"key": api_key.get(), "appid": game_id.get()})
        data = response.json()
        player_count = data["response"]["player_count"]
        
        # Update the player count label
        player_count_label.config(text=f"Current Players: {player_count}")
    except requests.exceptions.RequestException:
        player_count_label.config(text="Failed to retrieve player count")

# Create GUI window
window = tk.Tk()
window.title("Steam Game Player Count Tracker")

# Create input fields for API key and game ID
api_key_label = tk.Label(window, text="Steam API Key:")
api_key_label.pack()
api_key = tk.Entry(window)
api_key.pack(pady=5)

game_id_label = tk.Label(window, text="Game ID:")
game_id_label.pack()
game_id = tk.Entry(window)
game_id.pack(pady=10)

# Create player count label
player_count_label = tk.Label(window, text="Current Players: -", font=("Arial", 14))
player_count_label.pack(pady=20)

# Create update button
update_button = tk.Button(window, text="Update", command=update_player_count)
update_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
