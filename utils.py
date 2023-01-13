import spotipy as sp
import pandas as pd
import numpy as np

def get_album_track_features(album_url):
    album = sp.album(album_url)
    artist = album["artists"][0]["name"] 
    tracks = sp.album_tracks(album_url)
    track_list = tracks["items"]
    id_list = []
    for track in track_list:
      id_list.append(track["id"]) 
    feature_list = sp.audio_features(id_list)
    for i in range(len(feature_list)):
      feature_list[i]["track_name"] = sp.track(feature_list[i]["id"])["name"]
      feature_list[i]["artist"] = artist
    return feature_list

def clean_dataframe(df):
    return df.drop(["type", "id", "uri", "track_href", "analysis_url"], axis = 1)

def extract(url):
    return clean_dataframe(pd.DataFrame(get_album_track_features(url)))

def artist_tracks_df(id):
    albums = sp.artist_albums(id)["items"]
    df = extract(albums[0]["id"])
    for i in range(1, len(albums)):
        df = pd.concat([df, extract(albums[i]["id"])])
    return df

def playlist_tracks_df(url):
    tracks = sp.playlist_tracks(url)
    id_list = [track["track"]["id"] for track in tracks["items"]]
    feature_list = sp.audio_features(id_list)
    for i in range(len(feature_list)):
      feature_list[i]["track_name"] = sp.track(feature_list[i]["id"])["name"]
      feature_list[i]["artist"] = sp.track(feature_list[i]["id"])["artists"][0]["name"]
    return pd.DataFrame(feature_list).drop(["type", "id", "uri", "track_href", "analysis_url"], axis = 1)

   
    