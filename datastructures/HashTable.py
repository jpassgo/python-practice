class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    # Creates a list of tuples containing a key and a value
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Checks to see if an item with given key exists and updates that key if found. 
    # If key is new then that key value pair is added.
    def set_value(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            bucket[index] = (key, value)

        bucket.append((key, value))

    def get_value(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            return record_value
        else:
            return "No record found with that key value"

    def delete_value(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            while index < hash_table.size-1:
                print()
                self.hash_table[index] = self.hash_table[index+1]
                index += 1

    # Loops through tuples in list and prints them all.
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(10)
# print(hash_table)
hash_table.set_value('john@example.com', "Guitarist/Vocalist")
hash_table.set_value('paul@example.com', "Bassist/Vocalist")
hash_table.set_value('ringo@example.com', "Drummer")
hash_table.set_value('george@example.com', "Lead Guitarist")
# print(hash_table)
hash_table.set_value('george@example.com', "Lead Guitarist/Vocalist")
# print(hash_table)
# print(hash_table.get_value('george@example.com'))

print(hash_table)
hash_table.delete_value('george@example.com')
print(hash_table)