# 30% [%%%.......]
# Still loading...

def print_loading_bar(load_level: int):
    show_loading_cells = load_level // 10
    if load_level == 100:
        print("100% Complete!")
        print(f"[{'%' * 10}]")
    else:
        print(f"{load_level}% [{'%' * show_loading_cells}{'.' * (10 - show_loading_cells)}]")
        print("Still loading...")


loading = int(input())
print_loading_bar(loading)
