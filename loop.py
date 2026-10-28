# #  Find the maximum price from the list of dictionaries and return the dictionary with the maximum price.

# list = [
#     {
#         "name" : "raj",
#         "price" : 400
#     },
#     {
#         "name" : "rishabh",
#         "price" : 200
#     }
# ]

# max = list[0]["price"]
# listmax = list[0]
# for i in  list:
#     price = i["price"]
#     print(price > max)
#     if price < max:
#         max = price
#         listmax = i
#         # print(i)
# print(listmax)

# --------------------------------------------------------------------------------------------------------

# # find the total price of all the items in the list of dictionaries and return the total price.

# list = {
#     "fan":100,
#     "cooler":300,
#     "T.V":2000,
#     "A.C":3000
# }

# discount = []
# total_price = 0
# for i in list:
#     total_price += list[i]
#     if list[i] >= 1000:
#         discount.append(int(list[i] * 0.10))
#     else:
#         discount.append(0)
#         print(f"{i} : {list[i]}")

# print(f"Total price  is : {total_price}")

# total_discount = 0
# for i in discount:
#     total_discount += i
# print(f"Total discount  is : {total_discount}")
# print(f"Final payable amount : {total_price - total_discount}")
# for (k,v),d in zip(list.items(),discount):
#     print(k,v,d)

# --------------------------------------------------------------------------------------------------------

## right triangle pattern

# for i in range(1, 5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# --------------------------------------------------------------------------------------------------------

##  remove negative numbers from the list
# list1 = [1,2,3,4,5,-1,-2,-3,-4,-5]
# for i in list1[:]:
#     if i < 0:
#         list1.remove(i)
# print(list1)

# --------------------------------------------------------------------------------------------------------

##
tuple1 = (1,2,3,4,5,6)
sum = 0
for i in tuple1:
    if i%2 == 0 :
          sum += i
  
print(sum)


