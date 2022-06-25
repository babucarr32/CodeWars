
def maskify(cc):
    return  cc[:4] + ("*" * (len(cc)-4))
print(maskify("1234567"))