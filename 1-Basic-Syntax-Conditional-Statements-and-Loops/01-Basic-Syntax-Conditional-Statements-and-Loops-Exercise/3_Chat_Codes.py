messages_sent = int(input())

for i in range(1, messages_sent + 1):
    n = int(input())
    current_message = ''
    if n == 88:
        current_message = 'Hello'
    elif n == 86:
        current_message = 'How are you?'
    elif n < 88 and not n == 86:
        current_message = 'GREAT!'
    elif n > 88:
        current_message = 'Bye.'
    print(f'{current_message}')