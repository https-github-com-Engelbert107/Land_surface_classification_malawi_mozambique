
from src.function_display_map import display_map

from config import args


def main(args):

    display_map(args.geojson_file, args.latitude, args.longitude)



if __name__ == "__main__":
    main(args)