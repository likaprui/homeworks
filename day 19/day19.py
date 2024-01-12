# def zipp(a, b, c):
#     d = []
#     result= ""
#     i=0
#     max_len= max(len(a), len(b), len(c))
#     min_len= min(len(a), len(b), len(c))
#     while i < len(a):
#         result=a[i]+ str(b[i])+ c[i]
#         i+=1
#         d.append(result)
#         result=""
#         # d.append(a[-1])            
#         return d
    
#     # for i in range(min_len, max_len):
#     #     d.append([i])
#     #     return d
    
# a = ["a", "b", "c", "d"]
# b = [ 1, 2, 3, 4]
# c = ["sandro", "misha", "dato", "nika"]
# print(zipp(a, b ,c))





# a = ["a", "b", "c", "d"]
# b = [ 1, 2, 3, 4]
# c = ["sandro", "misha", "dato", "nika", "simba"]
# d=[]


# #თუ ყველაზე პატარა სია არის a
# if len(a) < len(b) and len(a) < len(c):
#     for i in range(len(a)):
#         d.append(str(a[i]) + str(b[i])+ str(c[i]))
#     for i in range (len(b), len(c)):
#         d.append(str(b[i]) + c[i])

# #თუ ყველაზე პატარა სია არის b
# elif len(b) < len(a) and len(b) < len(c):
#     for i in range(len(b)):
#         d.append(str(a[i]) + str(b[i]) + str(c[i]))
#     for i in range (len(a), len(c)):
#         d.append(str(a[i]) + c[i])

# #თუ ყველაზე პატარა სია არის c
# elif len(c) <= len(b) and len(b) < len(a):
#     for i in range (len(c)):
#         d.apppend(str(a[i]) + str(b[i]) + str(c[i]))
#     for i in range(len(b), len(a)):
#         d.append(str(b[i]) + a[i])
# print(d)


# def math(a, b, c):
#     return max(a -b +c, a+b *c, (a+b) - c, a *(b+c))
# print(math(16,15,34)-math(37, 21, 1)-math(14,1,6)+-69)

# print(15*16*30-17*20*3-15*5*2)

# print(16*15*34-37*21-14*6-69)


# def sum_mixe(arr):
#     final_sum =0
#     for num in arr:
#         final_sum+= int(num)
#     return final_sum
# print(sum_mixe(["7", 9, 2, 1]))
