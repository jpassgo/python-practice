
def generate_parentheses():       
    print(back_track())
    return 1

def back_track(well_form_parentheses = [], s = [], left = 0, right = 0, n: int = 3):
    if len(s) == 2 * n:
        print(s)
        print("\n")
        well_form_parentheses.append("".join(s))
        return
    if left < n:
        print(s)
        print("\n")
        s.append("(")
        print(s)
        print("\n")
        back_track(well_form_parentheses, s, left+1, right, n)
        s.pop()
        print(s)
        print("\n")
    if right < left:
        print(s)
        print("\n")
        s.append(")")
        print(s)
        print("\n")
        back_track(well_form_parentheses, s, left, right+1, n)
        s.pop()
        print(s)
        print("\n")
    
    return well_form_parentheses


generate_parentheses()