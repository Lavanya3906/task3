import tkinter as tk
from tkinter import messagebox
from lyricsgenius import Genius

def get_lyrics():
    title = title_entry.get()
    artist = artist_entry.get()

    if not title or not artist:
        messagebox.showerror("Error", "Please enter both title and artist.")
        return

    try:
        genius = Genius("your_access_token_here")
        song = genius.search_song(title, artist)
        if song:
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, song.lyrics)
        else:
            messagebox.showerror("Error", "Lyrics not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Lyrics Extractor")

# Create labels and entry fields
tk.Label(root, text="Title:").grid(row=0, column=0, sticky="w")
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Artist:").grid(row=1, column=0, sticky="w")
artist_entry = tk.Entry(root)
artist_entry.grid(row=1, column=1)

# Create a button to trigger lyrics extraction
extract_button = tk.Button(root, text="Get Lyrics", command=get_lyrics)
extract_button.grid(row=2, columnspan=2)

# Create text area to display lyrics
lyrics_text = tk.Text(root, height=20, width=50)
lyrics_text.grid(row=3, columnspan=2)

root.mainloop()