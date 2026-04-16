my_set = {1,2,3}

my_set.add(7)
print(my_set)

my_set.remove(3)
print(my_set)

my_set.discard(8)
print(my_set)

print(len(my_set))

my_set.clear()
print(my_set)
print(len(my_set))

my_list = [1,2,2,2,4,5]
print(my_list)

listaUnike=set(set_list)

listaUnike2=list(listaUnike)

print(listaUnike)
print(listaUnike2)


user1_interest={"music","movies","travel"}
user2_interest={"music","movies","travel"}

rezultati = user1_interest.intersection(user2_interest)

print(rezultati)

users = {"tuana","zara","cakolli"}
personi = "tuana"
print(personi in user)
