import re

# Valid email format
# Email consists of two parts the `Local part` and the `Domain part`
# The local part can be up to 64 characters in length and consist of any combination of alphabetic characters, digits, or any of the following special characters:
# ! $ % & ‘ * + – / = ? ^ _ ` . { | } ~
# The domain part cannot be more than 255 characters in length and must conform to the specification for hostnames which is a list of dot-separated DNS labels.
# Each DNS label must not exceed 63 characters and should consist of any
# combination of alphabetic characters, digits and hypens.
def is_email_valid(email):
    email_parts = re.split('@', email)
    local_part = email_parts[0]
    domain_part = email_parts[1]
    # print(f"local_part= {local_part} : domain_part= {domain_part}")

    if(local_part_exceeds_character_limit(local_part)):
        return False

def local_part_exceeds_character_limit(local_part):
    return True if len(local_part) > 64 else False

is_email_valid("fakeemail@gmail.com")

print(is_email_valid("fakeadasfdsfdsafdsafdsasfdsdafadsfdsfdsafdsafdsafdsafdsafdsafdsaemail@gmail.com"))