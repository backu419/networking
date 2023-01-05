def add(num):
    return num + 10


price = [10, 20, 15, 13, 45, 16, 33]
# new_price = []
# for p in price:
#     new_price.append(add(p))
# print(new_price)
new_price = map(add,price)
print(list(new_price))

num=[10.233, 20.333, 15.56, 13.12, 45.10, 16.233, 33.011]
new_prices=map(lambda n:n+5, price)
round_num=list(map(round,num))
print(list(new_prices))
print(round_num)


def Task(num):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                # return num
                pass
                break
        else:
            return num

    else:
        pass

# Task(num)
task=[1,2,4,5,7,8,12,11]
ntask=list(map(Task,task))
print((ntask))

