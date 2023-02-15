# def get_volew_filter(function):
#     def wrapper():
#         letter = function()
#         return [let for let in letter if let in "acuoi"]
#     return wrapper
#
# @get_volew_filter
# def get_letter():
#     return ['a', 'b', 'c', 'd', 'e']
#
# print(get_letter())

def repeat(n):
    def decorator(fucntion):
        def wrapper():

