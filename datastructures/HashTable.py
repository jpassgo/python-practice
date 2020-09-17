class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_value(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        bucket.append((key, value))

    def get_value(self, key):
        pass

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(10)
print(hash_table)
hash_table.set_value('john@example.com', "Guitarist/Vocalist")
hash_table.set_value('paul@example.com', "Bassist/Vocalist")
hash_table.set_value('ringo@example.com', "Drummer")
hash_table.set_value('george@example.com', "Lead Guitarist")
print(hash_table)