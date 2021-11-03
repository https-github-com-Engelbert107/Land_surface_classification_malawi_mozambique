import landsatxplore
from landsatxplore.earthexplorer import EarthExplorer

from config import args



def Download_all_Landsat(args):
 
    api = landsatxplore.api.API(args.user, args.password)
 
    scenes = api.search(
        dataset = args.product,
        latitude = args.latitude,
        longitude = args.longitude,
        start_date = args.start_date,
        end_date = args.end_date,
        max_cloud_cover = args.cloud_max)
 
    print('{} scenes found.'.format(len(scenes)))
    api.logout()
 
    Earth_Down = EarthExplorer(args.user, args.password)
 
    for scene in scenes:
 
        #ID = scene['entityId']
        ID = scene['landsat_scene_id']
        print('Downloading data %s '% ID)
        
        # Download all data
        Earth_Down.download(ID, output_dir=args.output_dir)
 
    Earth_Down.logout()