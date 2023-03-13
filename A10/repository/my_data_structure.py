class MyDataStructure:
    def __init__(self):
        self.__objects = {}
        self.__it = None

    def __getitem__(self, key):
        if key in self.__objects:
            return self.__objects[key]
        return None

    def __setitem__(self, obj, value):
        self.__objects[obj] = value

    def __delitem__(self, obj):
        oldObject = self.__objects[obj]
        del self.__objects[obj]
        return oldObject

    def __next__(self):
        return self.__it.__next__()

    def __iter__(self):
        self.__it = self.__objects.values().__iter__()
        return self

    # self -> self.__next()
    # self.__it -> self.__it.__next()

    @staticmethod
    def filter_list(a_list, filter):
        filtered_list = []
        for it in a_list:
            if filter(it):
                filtered_list.append(it)
        return filtered_list

    @staticmethod
    def sort(a_list, compare):
        n = len(a_list)

        gap = n
        swapped = True

        while gap != 1 or swapped == 1:
            gap = (gap * 10) // 13
            if gap < 1:
                return a_list
            swapped = False

            for i in range(0, n - gap):
                # if a_list[i] > a_list[i + gap]:
                if compare(a_list[i], a_list[i + gap]):  # used
                    a_list[i], a_list[i + gap] = a_list[i + gap], a_list[i]
                    swapped = True
        return a_list
""""
a = MyDataStructure()

a['a']='1'
a['b']='2'
a['c']='3'
a['d']='4'

for i in a:
    i += 1

iter = a.__iter__()

i = iter.__next__()
while(i):

    i +=1
    i = iter.__next__()
"""