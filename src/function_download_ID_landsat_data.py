import random
import landsatxplore
from landsatxplore.earthexplorer import EarthExplorer

from config import args


def Download_ID_Landsat(args):
 
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
    
    # Number of dict in the list scenes
    res = len([elements for elements in scenes if isinstance(elements, dict)])

    # data filtering
    lis = []
    for i in range(res):
        lis.append(scenes[i]['landsat_scene_id'])
    print()
    print(lis)
    
    
    Earth_Down = EarthExplorer(args.user, args.password)

    ID = random.choice(lis)
    
    # Download a particular data
    Earth_Down.download(ID, output_dir=args.output_dir)

 
    Earth_Down.logout()