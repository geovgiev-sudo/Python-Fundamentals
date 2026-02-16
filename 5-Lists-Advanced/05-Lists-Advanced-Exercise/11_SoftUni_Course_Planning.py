def add_lesson(list_of_lessons: list, title: str) -> list:
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons: list, title: str, insert_index: int) -> list:
    if title not in list_of_lessons:
        list_of_lessons.insert(insert_index, title)
    return list_of_lessons


def remove_lesson(list_of_lessons: list, title: str) -> list:
    if title in list_of_lessons:
        list_of_lessons.remove(title)
        if f"{title}-Exercise" in list_of_lessons:
            list_of_lessons.remove(f"{title}-Exercise")
    return list_of_lessons


def swap_lesson(list_of_lessons: list, first_lesson: str, second_lesson: str) -> list:
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        first_has_exercise = f"{first_lesson}-Exercise" in list_of_lessons
        second_has_exercise = f"{second_lesson}-Exercise" in list_of_lessons
        # Swap lessons
        list_of_lessons[first_position], list_of_lessons[second_position] = \
            list_of_lessons[second_position], list_of_lessons[first_position]
        # Swap Exercises
        # Both lessons have exercise
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_position + 1], list_of_lessons[second_position + 1] = \
                list_of_lessons[second_position + 1], list_of_lessons[first_position + 1]
        # Only first lesson have exercise
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_position + 1, list_of_lessons.pop(first_position + 1))
        # Only second lesson have exercise
        elif second_has_exercise and not first_has_exercise:
            list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))
    return list_of_lessons


def exercise(list_of_lessons: list, title: str) -> list:
    exercise_name = f"{title}-Exercise"
    # We have title but have no exercise
    if title in list_of_lessons and exercise_name not in list_of_lessons:
        lesson_index = list_of_lessons.index(title)
        list_of_lessons.insert(lesson_index + 1, exercise_name)
    # We have no such lesson title in our schedule
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(exercise_name)
    # We don't need to modify our list in case
    # where we already have title and exercise in it
    return list_of_lessons


lessons = input().split(", ")
command = input().split(":")
while len(command) > 1:
    action = command[0]
    lesson_title = command[1]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        index = int(command[2])
        lessons = insert_lesson(lessons, lesson_title, index)
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        second_title = command[2]
        lessons = swap_lesson(lessons, lesson_title, second_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input().split(":")
for index, lesson in enumerate(lessons):
    print(f"{index + 1}.{lesson}")