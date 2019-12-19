if __name__ == "__main__":
    print()
    temps = [("Guwahati", 29), ("Dibrugarh", 36), ("Nagaon", 19), ("Tezpur", 26), ("Nalbari", 27), ("Shillong", 28), ("Barpeta", 22)]

    c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)
    
    c = list(map(c_to_f, temps))
    print(c)