class Solution:
    def remove_duplicates(self, s):
        result = []
        for char in s:
            if char not in result:
                result.append(char)
        return "".join(result)
    
    def find_min_max(self, s):
        min_num = min(s)
        max_num = max(s)
        return (max_num, min_num)

    def sort_by_second(self, s):
        return sorted(s, key=lambda x:x[1])


    def flatten(self, s):
        result = []
        for i in s:
            for j in i:
                result.append(j)
        return result
    
    def second_largest(self, s):
        sorted_s = sorted(list(set(s)))
        if len(sorted_s) < 2:
            return None
        return sorted_s[-2]

    def rotate_list(self,s,k,direction):
        if direction == 'right':
            return s[-k:]+s[:k+1]
        elif direction == 'left':
            return s[k:]+s[:k]
        
    def list_intersection(self, lst1, lst2):
        # result = []
        # for i in lst1:
        #     for j in lst2:
        #         if i == j and i not in result:
        #             result.append(i)
        # return result
        print(list(set(lst1) & set(lst2)))


    def group_anagrams(self,lst):
        result = {}
        for word in lst:
            sorted_word = "".join(sorted(word))
            print(sorted_word)
            if sorted_word not in result:
                result[sorted_word] = []
            result[sorted_word].append(word)
        return list(result.values())


    def remove_all_occurrences(self, lst , n):
        result = []
        for i in lst:
            if i != n:result.append(i)
        return result

    
    def find_pairs(self, lst, n):
        result = []
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i]+lst[j] == n:
                    result.append((lst[i], lst[j]))
        return result

    def remove_consecutive_duplicates(self, lst):
        if not lst:
            return []
        result = []
        result = [lst[0]]
        for i in range(1, len(lst)):
            if lst[i] != lst[i-1]:
                result.append(lst[i])
        return result
                    

    def two_largest(self, lst):
        if not lst or len(lst) < 2:
            return None
        sorted_lst = sorted(set(lst))
        return sorted_lst[-2:]

    def sort_by_second_desc(self, lst):
        sorted_lst = sorted(lst, key=lambda a : a[1], reverse=True)
        return sorted_lst

    def flatten(self, lst):
        result = []
        for i in lst:
            if isinstance(i, list):
                result.extend(self.flatten(i))
            else:
                result.append(i)
        return result
    
    def third_largest(self, lst):
        sorted_lst = sorted(set(lst))
        if len(sorted_lst) < 3:
            return None
        return sorted_lst[-3]

    def rotate_left(self, lst, k):
        return lst[k:]+lst[:k]

    def list_difference(self, lst1, lst2):
        return list(set(lst1)-set(lst2))

    def unique_anagrams(self, lst):
        result = {}
        for word in lst:
            sorted_word = "".join(sorted(word))
            if sorted_word not in result:
                result[sorted_word] = []
            result[sorted_word].append(word)
        return list(result.values())

    def remove_condition(self, lst, condition):
        return [x for x in lst if not condition(x)]

    def find_pairs_with_difference(self, lst, n):
        result= []
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if abs(lst[i]-lst[j])==n:
                    result.append((lst[i],lst[j]))
        return result

    def print_triagle(self):
        for i in range(1, 8):
            print("*"*i)



sol = Solution()
# print(sol.remove_duplicates(["a", "b", "a", "c", "b"]))  # Output: ['a', 'b', 'c']
# print(sol.find_min_max([2, 8, 1, 6, -4, 10]))
# print(sol.sort_by_second([(1, 3), (4, 2), (5, 1)]))
# print(sol.flatten([[1, 2, 3], [4, 5], [6, 7, 8]]))
# print(sol.second_largest([10, 20, 4, 45, 99]))
# print(sol.rotate_list([1, 2, 3, 4, 5], 2,'left'))
# print(sol.list_intersection([1, 2, 2, 3, 4], [2, 3, 5, 7]))
# print(sol.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(sol.remove_all_occurrences([1, 2, 3, 4, 3, 5], 3))
# print(sol.find_pairs([1, 2, 3, 4, 5], 6))
# print(sol.remove_consecutive_duplicates([1, 2, 2, 3, 2, 4, 4, 5, 5,6,7,7,8]))
# print(sol.two_largest([10, 20, 20, 4, 45, 99, 99]))
# print(sol.sort_by_second_desc([(1, 3), (4, 2), (5, 1)]))
# print(sol.flatten([1, [2, [3, [4, 5]], 6], 7]))
# print(sol.third_largest([10, 20, 4, 45, 99]))
# print(sol.rotate_left([1, 2, 3, 4, 5], 2))
# print(sol.list_difference([1, 2, 3, 4], [2, 3, 5]))
# print(sol.unique_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(sol.remove_condition([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) )
# print(sol.find_pairs_with_difference([1, 5, 3, 4, 2], 2) )
print(sol.print_triagle())

