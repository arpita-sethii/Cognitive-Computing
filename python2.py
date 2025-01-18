import random

def list_opr():
    num = [10,20,30,40,50,60,70,80]
    num.append(200) 
    num.append(300)
    num.remove(10) 
    num.remove(30)
    num.sort()
    print("Sorted:" ,num)
    num.sort(reverse=True)
    print("Descending: ", num)

list_opr()
    
def tuple_opr():
    scores=(45,89.5,76,45.4,89,92,58,45)
    max_score=max(scores)
    print(max_score)
    min_score=min(scores)
    print(min_score)
    max_index=scores.index(max_score)
    print(max_index)
    min_count=scores.count(min_score)
    print(min_count)
    reversed_list= list(scores[::-1])
    print(reversed_list)

    u_input=76
    if u_input in scores:
        print(f"{u_input} found at index {scores.index(u_input)}")
    else:
        print(f"{u_input} not found in scores")

tuple_opr()

def random_num():
    num=[random.randint(100,900) for _ in range(100)]
    odd_n=[ number for number in num if number%2==1]
    print("Odd Numbers are: ",odd_n)
    even_n=[ number for number in num if number%2==0 ]
    print("Even Numbers are: ",even_n)
    prime_n=[ number for number in num if number >1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))]
    print("Prime Numbers are: ",prime_n)

random_num()

def set_opr():
    A= {34,56,78,99}
    B= {78,45,90,23}
    print("Union: " , A|B)
    print("Intersection: ", A & B)
    print("Symmetric Difference: ", A ^ B)
    print("S1 is subset of S2", A.issubset(B))
    print("S2 is super set of S1", A.issuperset(B))
    
    X=56
    if X in A:
        A.remove(X)
    else:
        print(f"{X} not present in A")
    print("Updated A:", A)

set_opr()

def dict_opr():
    data = {"city": "New York", "population":8419600, "area": 468.9}
    data["location"]= data.pop("city")
    print("updated: ", data)

dict_opr()