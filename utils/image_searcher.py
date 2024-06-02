import pandas as pd

def search_url(model_name, PATH_CATALOG):
    
    df = pd.read_csv(PATH_CATALOG)
    match = df[df['model_name'] == model_name]
    
    if not match.empty:
        return match.iloc[0]['url_media']
    else:
        return "https://m.media-amazon.com/images/I/618iVz7RxwL.jpg"