import argparse

GENRE = {
    "a": "action",
    "c": "comedy",
    "t": "thriller",
    "f": "fantastic",
}

WEEK_DAY = {
    "m": "monday",
    "f": "friday",
    "s": "saturday",
    "su": "sunday",
}

CITY = {
    "p": "Plovdiv",
    "v": "Varna",
    "s": "Sofiq"
}


def make_ticket(processed_output):
    ticket = f"{GENRE[processed_output.genre]} movie on {WEEK_DAY[processed_output.day_of_week]} in {CITY[processed_output.city]}"

    if processed_output.bonus:
        ticket += ' with bonus beer and chips '
    if processed_output.comment:
        ticket += 'Your comment is: '
        ticket += ' '.join(processed_output.comment)
    return ticket


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to ARENA CINEMA")
    parser.add_argument("genre", type=str, choices=GENRE.keys(), help="What kind of movies do you want to watch")
    parser.add_argument("day_of_week", type=str, choices=WEEK_DAY.keys(), help="Choose day of weeks")
    parser.add_argument("city", type=str, choices=CITY.keys(), help="Choose city")
    parser.add_argument("-bonus", '-b', action='store_true', dest='bonus', help="week bonus is beer and chips"  )
    parser.add_argument("--comment", "-c", type=str, nargs="+", dest='comment', help="Do you need 3d glasses")
    parsed_args = parser.parse_args()
    print(make_ticket(parsed_args))