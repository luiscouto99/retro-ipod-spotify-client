#!/usr/bin/env python3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# ====== CONFIG ======
CACHE = ".cache"  # make sure this is your OAuth cache file from earlier
DEVICE_NAME = "Spotipod"  # must match librespot device name exactly
SCOPE = "user-modify-playback-state,user-read-playback-state"

# ====== WAIT FOR LIBRESPOT ======
time.sleep(10)  # wait 10s to let librespot register on Spotify

# ====== AUTH ======
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, cache_path=CACHE))

# ====== GET DEVICES ======
devices = sp.devices()["devices"]
print("Available devices:", devices)

# ====== FIND PI DEVICE ======
pi_device = next((d for d in devices if d["name"] == DEVICE_NAME), None)

if pi_device:
    # Transfer playback to Pi
    sp.transfer_playback(pi_device["id"], force_play=True)
    print(f"Playback transferred to {DEVICE_NAME}")
else:
    print(f"{DEVICE_NAME} not found. Make sure librespot is running.")
