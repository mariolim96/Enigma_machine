import string

def shift(r1, idx):
    for i in range(2):
        r1[i] = r1[i][idx:]+r1[i][:idx]
    return r1

# set the rotor by key
def setup_rotors(r1, r2, r3, a, b, c):
    print(r1[0].find("D"))
    r1 = shift(r1, r1[0].find(a))
    r2 = shift(r2, r2[0].find(b))
    r3 = shift(r3, r3[0].find(c))
    print(r1, r2, r3)
    return r1, r2, r3
    
# rotor mechanism    
def shift_rotors(r1, r2, r3,a="V",b="E",c="Q"):
   
    if r3[0][0] == a:
        r3 = shift(r3, 1)
        if r2[0][0] == b:
            r2 = shift(r2, 1)
            if r1[0][0] == c:
                r1 = shift(r1, 1)
                r3 = shift(r3, 1)
                return r1, r2, r3
            else:
                r3 = shift(r3, 1)
                return r1, r2, r3
        else:
            r2 = shift(r2, 1)
            return r1, r2, r3
    r3 = shift(r3, 1)
    return r1, r2, r3

def find_index_reflector(idx,reflector=REFLECTOR):
    # find the same letter but with another index
    letter = reflector[idx];
    for i, val in enumerate(reflector):
        if i != idx and letter == val:
            
            return i

# pass through side of a rotor 
def find_index_rotor(r1, r2, idx):
   
    letter = r1[idx];print(letter,"lettera r1")
    idx = r2.find(letter);print(idx,"indice lettera r1b\n")
    return idx

# go through the 3 rotors and find the last index
def find_letter(r1, r2, r3, idx, coding=False):
    
    if coding:
        idx = find_index_rotor(r1[0], r1[1], idx)
        idx = find_index_rotor(r2[0], r2[1], idx)
        idx = find_index_rotor(r3[0], r3[1], idx)
        return idx
    idx = find_index_rotor(r1[1], r1[0], idx)
    idx = find_index_rotor(r2[1], r2[0], idx)
    idx = find_index_rotor(r3[1], r3[0], idx)
    return idx


def enigma(r1, r2, r3, word, reflector=REFLECTOR, a=ALPHABET):
    
    crit = ''
    for i in word:
        r1, r2, r3 = shift_rotors(r1, r2, r3)
        idx_a = find_letter(r3, r2, r1, a.find(i))
        idx_a = find_index_reflector(idx_a)
        idx_a = find_letter(r1, r2, r3, idx_a, True)
        crit = crit + a[idx_a]
    return crit
def partial():
    return

if __name__ == "__main__":
    
    ALPHABET = string.ascii_uppercase
    REFLECTOR = "ABCDEFGDIJKGMKMIEBFTCVVJAT"
    rotor = [[string.ascii_uppercase, "EKMFLGDQVZNTOWYHXUSPAIBRCJ"],
             [string.ascii_uppercase, "AJDKSIRUXBLHWTMCQGZNPYFVOE"],
             [string.ascii_uppercase, 'BDFHJLCPRTXVZNYEIWGAKMUSQO']]
    
    word = "ENIGMADJKJALALANDNLFNLAKLAJFLAHKAHFLFLAALFHLHALAL"
    word="GSPHDXXPIQVDZIXACTSQLSTGEIBIAUXYKRWRLYJKIJNIRNADA"
    
    rotor = setup_rotors(rotor[0], rotor[1], rotor[2], "D", "O", "G")
    enigma1 = enigma(rotor[0],rotor[1],rotor[2],"ENIGMA")
    rotor = setup_rotors(rotor[0], rotor[1], rotor[2], "D", "O", "G")
    cripted = enigma(rotor[0],rotor[1],rotor[2],"GSPHDX")
    print(enigma1,cripted)

