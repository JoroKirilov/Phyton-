import argparse

SIZES = {
    "s": "Small",
    "m": "Medium",
    "l": "Large",
    "xl": "Extra Large",
    "xxl": "Extra Extra Larga"
}

COLORS = {
    'w': "White",
    'b': "Black",
    'r': "Red"
}


def make_shirt(processed_output):
    shirt = f"{SIZES[processed_output.size]} {COLORS[processed_output.color]} shirt: "
    if processed_output.custom:
        shirt += ', '.join(processed_output.custom)
    if processed_output.logo:
        shirt += ' with logo'
    if processed_output.fabric:
        shirt += ' and soft fabric'
    return shirt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to the custom shirt factory")
    parser.add_argument("size", type=str, choices=SIZES.keys(), help='Size of your shirt')
    parser.add_argument('color', type=str, choices=COLORS.keys(), help="Color or your shirt")
    parser.add_argument('-l', '--logo', action='store_true', dest='logo', help="add logo to your shirt")
    parser.add_argument('--soft-fabric', action='store_true', dest='fabric', help='Makes your shirt softer')
    parser.add_argument('-c', '--custom', type=str, dest='custom', nargs="+", help='Customise your shirt')
    parsed_args = parser.parse_args()
    print(make_shirt(parsed_args))