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


def caesarCipher(string, k):
    length = len(string)
    for i in range(length):
        if 97 <= ord(string[i]) <= 122:
            _ascii = ord(string[i])
            string = string[:i]+chr((((_ascii-97)+k) % 26)+97)+string[i+1:]
            # print(string)
        elif 65 <= ord(string[i]) <= 90:
            _ascii = ord(string[i])
            string = string[:i]+chr((((_ascii-65)+k) % 26)+65)+string[i+1:]
            # print(string)
    # print("\n")
    print(string)


if __name__ == "__main__":
    string = "middle-Outz"
    k = 3
    print("\n")
    caesarCipher(string, k)
    print("\n")