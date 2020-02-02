# input :       11
#               middle-Outz
#               2
# ouput :       okffng-Qwvb
# explanation : Original alphabet:      abcdefghijklmnopqrstuvwxyz
#               Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

#               m -> o
#               i -> k
#               d -> f
#               d -> f
#               l -> n
#               e -> g
#               -    -
#               O -> Q
#               u -> w
#               t -> v
#               z -> b


# this partial correct form of answer but logic can be quite satisfying as a beginner

def caesarCipher(string, k):
    abcd = "abcdefghijklmnopqrstuvwxyz"
    abcd_len = len(abcd)
    origin = ""
    rotate = ""
    i = 0

    while i < abcd_len:
        if i == k:
            rotate = abcd[0:k]
            origin = abcd[k:abcd_len]
        i = i+1
    
    new_abcd = origin+rotate
    # print(new_abcd)


    i = 0
    strlen = len(string)
    cipher = ""
    while i < strlen:
        j = 0
        while j < abcd_len:
            if string[i] == abcd[j]:
                cipher = cipher+new_abcd[j]
                break
            if string[i] == abcd[j].upper():
                cipher = cipher+new_abcd[j].upper()
                break
            elif 31 < ord(string[i]) < 65:
                cipher = cipher+string[i]
                break
            j = j+1
        i = i+1
    
    print(cipher)


if __name__ == "__main__":
    string = "middle-Outz"
    k = 3
    print("\n")
    caesarCipher(string, k)
    print("\n")