def new_password(n):
    password = []
    for i in range(1, 20):
        for j in range(i + 1, 21):
            if (i + j) % n == 0:
                password.append(str(i))
                password.append(str(j))
    return ''.join(password)

print(new_password(9))
print(new_password(11))