def echo(text: str, repetititons: int = 3) -> str:
    """Imitate a real-world echo"""
    echos = ""
    def repeat(i):
        return f"{text[i:]}\n"

    for i in range(-repetititons, 0, 1):
        echos += repeat(i)
    return echos

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))