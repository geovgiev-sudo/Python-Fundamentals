def data_type_integer(number: int) -> int:
    return number * 2


def data_type_real(number: float) -> float:
    return number * 1.5


def data_type_string(string: str) -> str:
    return f"${string}$"

data_type = input()
data_input = input()
if data_type == "int":
    print(data_type_integer(int(data_input)))

elif data_type == "real":
    print(f"{data_type_real(float(data_input)):.2f}")

elif data_type == "string":
    print(data_type_string(data_input))