from wf_datagen import fetch_and_save_anime_data
from wf_dataprocessing import process_data
from wf_visualization import visualize_data

"""
DESC: fetch_and_save_anime_data is commented out since it uses the Jikan API to fetch data. 
It fetches data page by page, with a total of 1102 pages. 
The Jikan API has limitations on how many requests can be made, so after each API call, the script sleeps for 1 second. 
The total time taken for the entire data collection was 55 minutes.
"""
# fetch_and_save_anime_data()
process_data()
visualize_data()
