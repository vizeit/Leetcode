def defangIPaddr(address: str) -> str:
    return ''.join('[.]' if c == '.' else c for c in address)

if __name__ == "__main__":
    print(defangIPaddr("1.1.1.1"))
    print(defangIPaddr("255.100.50.0"))