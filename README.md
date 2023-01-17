## PREDICTION OF MUSIC GENRE BASED ON AUDIO FEATURES PROVIDED BY SPOTIFY
---
`data_retrieval.ipynb`: features of the tracks obtained via spotify API

`genre_classification.ipynb`: data analysis and the training of model

`usecases.ipynb`: model is used for 2 purposes

`environment.yml`: environment file

`genre_df.csv`: tracks with their audio features

`model.dat`: stored model in binary file

### To get Spotify API to work, you must make an account/project @ [Spotify for Developers](https://developer.spotify.com/)

#### Create a project, set the `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET` environment varaiables as given in the project (under dashboard), AND `SPOTIPY_REDIRECT_URI` as any valid URI

#### [Authorization for Spotipy](https://spotipy.readthedocs.io/en/2.11.2/#authorization-code-flow)