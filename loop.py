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

## sum of even number of tuple

# tuple1 = (1,2,3,4,5,6)
# sum = 0
# for i in tuple1:
#     if i%2 == 0 :
#           sum += i
  
# print(sum)

# --------------------------------------------------------------------------------------------------------

## reverse the list whitout reveres() and sort()

# list1 = [1,2,3,4,5]
# temp = []
# for i in list1:
#     temp.insert(0,i)
# print(temp)

# --------------------------------------------------------------------------------------------------------

## employee salary report

# total_company_salary = 0
# for i in range(1,5):
#     print(f"Enter salary for Emplotee {i} :")
#     total_salary = 0
#     for j in range(1,4):
#         salary = int(input(f"Month {j} : "))
#         total_salary += salary
#     print(f"Total Salary : {total_salary}")
#     total_company_salary += total_salary
#     if total_salary > 60000:
#         print("High Earner")
#     print()
# print(f"Total Company Salary : {total_company_salary}")
# print()

# --------------------------------------------------------------------------------------------------------

## Triangle pattern

# r=5
# for i in range(1,r+1):
#     s=r-i
#     st=2*i-1
#     print(" " * s,end=" ")
#     print("*" * st)
    
# --------------------------------------------------------------------------------------------------------

## count and display duplicate numbers from the list without using set() and count() function.

# duplicate_list = []
# count = 0
# list1 = [1,2,3,4,4,5,1,5,2]
# for i in range(len(list1)):
#     dup = list1[i]
#     index = i
#     for m in range(index + 1,len(list1)):
#         if dup == list1[m]:
#            duplicate_list.append(dup)
#            count += 1
# print(f"Duplicate Number : {duplicate_list}")
# print(f"Duplicate Count : {count}")

# --------------------------------------------------------------------------------------------------------

## find common elements from two lists and return the common elements in a new list without using set() function.

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,4,5]
# common_list = []
# for i in list1:
#     for j in list2:
#         if i == j :
#             common_list.append(i)
# print(common_list)

# --------------------------------------------------------------------------------------------------------
