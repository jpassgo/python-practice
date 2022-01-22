
# Step One:
# Build a dictionary where the key is a requirement and the value is a list of the blocks where that requirement is present.
# E.g. 
# block_dict['gym'] = [2, 5]
# block_dict['store'] = [1, 3, 5]
# block_dict['office'] = [3, 4]

# Step Two:
# Sum the block number for each requirement in the block_dict with other block number of the other requirements and the answer
#   should be the median block number for the blocks with the lowest sum.
# This is not very efficient, the time complexity is something on the order of n^3

def best_apartment(blocks, reqs):

    block_dict = {}

    for i in range(len(blocks)-1):
        for key in blocks[i].keys():
            # If requirement is present on this block
            if blocks[i][key]:
                if key in block_dict:
                    block_dict[key].append(i)
                else:
                    block_dict[key] = [i]

    
blocks = [
    {
        'gym': False,
        'store': True,
        'office': False
    },
    {
        'gym': True,
        'store': False,
        'office': False
    },
    {
        'gym': False,
        'store': True,
        'office': True
    },
    {
        'gym': False,
        'store': False,
        'office': True
    },
    {
        'gym': True,
        'store': True,
        'office': False
    },
]


reqs1 = ['gym', 'store']
reqs2 = ['gym', 'store', 'office']


best_apartment(blocks, reqs1)