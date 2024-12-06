class Solution(object):
    def character_occurance(self, str):
        result = {}
        for char in str:
            if char in result:
                result[char]+=1
            else:
                result[char]=1
        return result
    
    def store_profile(self, lst):
        # result = {}
        # for i,j in lst:
        #     result[i] = j
        # return result
        return dict(lst)
    
    def most_frequent_word(self,lst):
        word_count = {}
        for word in lst:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        max_count = max(word_count.values())
        for w,c in word_count.items():
            if c == max_count:
                return w
            
    def store_product(self,lst):
        product_info = {}
        for product,price in lst:
            product_info[product]= price
        return product_info

    def sold_amount(self, lst):
        result = {}
        for product, amount in lst:
            if product in result:
                result[product]+= amount
            else:
                result[product] = amount
        return result
    
    def age_update(self, user_profiles, user_id, age):
        if not isinstance(user_id,int) or not isinstance(age,int):
            print("Could not find user profile")
            return False

        if user_id in user_profiles:
            name,_ = user_profiles[user_id]
            user_profiles[user_id] = (name,age)
            return user_profiles
        else:
            print("Could not find user profile")
            return False

    
    def max_key(self, s):
        max_value = max(s.values())
        for key, value in s.items():
            if value == max_value:
                return key

    def common_values(self, dict1, dict2):
        return list(set(dict1.values()) & set(dict2.values()))

    def track_orders(self, lst):
        result = {}
        for id, product in lst:
            print(id,product)
            if id not in result:
                result[id] = {product:1}
            else:
                if product not in result[id]:
                    result[id][product] = 1
                else:
                    result[id][product]+=1
        return result

s = Solution()
# print(s.character_occurance("abacabad"))
# print(s.store_profile([('Alice', 25), ('Bob', 30), ('Charlie', 35)]))
# print(s.most_frequent_word(['apple', 'banana', 'orange', 'banana']))
# print(s.store_product([('iPhone', 999), ('MacBook', 1299), ('iPad', 499)]))
# print(s.sold_amount([('apple', 10), ('banana', 5), ('apple', 20), ('orange', 8)]))
# users = {1: ('Alice', 25), 2: ('Bob', 30)}
# print(s.age_update(users, 1, 29))
# print(s.max_key({'a': 10, 'b': 20, 'c': 15, 'd':50}))
# dict1 = {'apple': 10, 'banana': 25, 'orange': 30}
# dict2 = {'banana': 25, 'orange': 30, 'pear': 15}
# print(s.common_values(dict1,dict2))
print(s.track_orders([(1, 'apple'), (2, 'banana'), (1, 'apple'), (1, 'orange')]))
