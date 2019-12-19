import statistics

if __name__ == "__main__":
    print()
    data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
    avg = statistics.mean(data)
    print(avg, "\n")

    c = list(filter(lambda x: x > avg, data))
    print(c)

    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

    names = ['', 'Max', 'Maddy', 'Madhu', '', '', '', '', 'Madhurjya']

    c1 = list(filter(None, names))
    print(c1)