from cipher import feistel_encode

if __name__ == "__main__":
    print(feistel_encode(200, 300))
    print(feistel_encode(int(2e10), 28))