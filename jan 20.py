class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


    def __str__(self):
        return str(self.__tags)
cloud = TagCloud()
cloud.add("python")

# # Iterating over the tags using a loop
# for tag in cloud:
#     print(tag)
#
# # print("length", len(cloud))
# # cloud["python"] = 5
cloud.add("python")
cloud.add("python")

# Printing the updated tags dictionary
# print(cloud.__tags["PYTHON"])
print(cloud)