def new_password(oldPassword, newPassword):
    if newPassword != oldPassword and len(newPassword) > 6:
        print(True)
    else:
        print(False)

new_password('boi','boiasdo')