# 
# Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, 
# the ID of the user making the access, and the resource ID. 
# The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.
#
# Example:
# logs1 = [
#     ["58523", "user_1", "resource_1"],
#     ["62314", "user_2", "resource_2"],
#     ["54001", "user_1", "resource_3"],
#     ["200", "user_6", "resource_5"],    
#     ["215", "user_6", "resource_4"],
#     ["54060", "user_2", "resource_3"],
#     ["53760", "user_3", "resource_3"],
#     ["58522", "user_22", "resource_1"],
#     ["53651", "user_5", "resource_3"],
#     ["2", "user_6", "resource_1"],
#     ["100", "user_6", "resource_6"],
#     ["400", "user_7", "resource_2"],
#     ["100", "user_8", "resource_6"],
#     ["54359", "user_1", "resource_3"],
# ]
# Example 2:
# logs2 = [
#     ["300", "user_1", "resource_3"],
#     ["599", "user_1", "resource_3"],
#     ["900", "user_1", "resource_3"],
#     ["1199", "user_1", "resource_3"],
#     ["1200", "user_1", "resource_3"],
#     ["1201", "user_1", "resource_3"],
#     ["1202", "user_1", "resource_3"]
# ]
# Example 3:
# logs3 = [
#     ["300", "user_10", "resource_5"]
# ]
# 
# Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, 
# together with how many accesses it saw.
# Expected Output:
# most_requested_resource(logs1) # => ('resource_3', 3)
# Reason: resource_3 is accessed at 53760, 54001, and 54060
# most_requested_resource(logs2) # => ('resource_3', 4)
# Reason: resource_3 is accessed at 1199, 1200, 1201, and 1202
# most_requested_resource(logs3) # => ('resource_5', 1)
# Reason: resource_5 is accessed at 300
# Complexity analysis variables:
# n: number of logs in the input


def access_times(access_logs):
    structured_logs = {}
    for access in access_logs:
        current_resource = ''
        current_time = ''
        for item in access:
            if item.startswith('re'):
                current_resource = item
            elif item.startswith('user'):
                break
            else:
                current_time = item

        if current_resource in structured_logs:
            structured_logs[current_resource] = [current_time]
        else:
            logs = structured_logs[current_resource]
            structured_logs[current_resource] = logs + current_time

    print(structured_logs)


logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],    
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]

access_times(logs1)