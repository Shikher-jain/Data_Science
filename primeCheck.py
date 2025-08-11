# def is_prime(n):
#     if n < 2:
#         return False
#     if n in (2, 3):
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False

#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# # print(is_prime(int(input('enter No.'))))
# print([is_prime(x) for x in range((int(input('enter No.'))))])


# d = {}
# print(type(d))
# d = {1}
# print(type(d))

# s ="abcd"
# for i in s:
    
#     d[i] += 1
# print(d)

# from collections import Counter
# from collections import defaultdict

# d=defaultdict(int)

# s = "abcd"
# for i in s:
#     d[i] += 1
# print(d)
# print(dict(d))

# s = "abcaad"
# d = Counter(s)
# print(dict(d))


# d = {}
# s = "abcd"
# for i in s:
#     d[i] = d.get(i, 0) + 1
# print(d)



# d = {}
# s = "aaaabcd"
# s = "aaaabcd"
# for i in range(len(s)):
#     d[s[i]] = d.get(s[i], 0) + 1
#     d[t[i]] = d.get(t[i], 0) + 1
# print(d)


# print([x for x in zip('egg','foo')])

# n = 1234321
# n1 = 12343
# n = str(n)
# print(n == (n[::-1]))

# i =0
# while n := 10 >i:
#     print(i)
#     i+=11
# print(n,i)

n =121

while True: 
    t = n*1+(n%10)
    n = n//10
print(t,n)




# s = ' im  dgvb dyugb dkjb  ,msuhu/djficm\\ jnedc je'
# print[s[1]]