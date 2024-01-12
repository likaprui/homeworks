# ორგანზომილებიანი სია ..
# def quarter_of(month):
#     months=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
#     if month in months[0]:
#         return 1
#     elif month in months[1]:
#         return 2
#     elif month in months[2]:
#         return 3
#     else:
#         return 4
# print(quarter_of(6))



# def remove_exclamation_marks(s):
#     # return s.replace("!", " ")
#     new_str=""
#     for char in(s):
#         if char!="!":
#             new_str+=char
#     return new_str
# print(remove_exclamation_marks("vauuu!"))




# def update_light(current):
#     traffic_lights=["red", "yellow", "green"]
#     if current == "red":
#         return "green"
#     return traffic_lights[traffic_lights.index(current)-1]
# print(update_light("yellow"))


# # sum without highest and lowest number
# def sum_array(arr):
#     if not arr:
#         return 0
#     elif len(arr) < 2:
#         return 0
#     arr.sort()
#     arr.pop(0)
#     arr.pop(-1)
#     return sum(arr)
# print(sum_array([2,3,4,1,7,6,9]))




