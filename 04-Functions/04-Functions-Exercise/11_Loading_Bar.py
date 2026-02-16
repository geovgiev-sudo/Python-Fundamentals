def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    number_of_percents = some_number // 10
    number_of_dots = 10 - number_of_percents
    return f"{some_number}% [{'%' * number_of_percents}{'.' * number_of_dots}]\nStill loading..."



number = int(input())
print(loading_bar(number))