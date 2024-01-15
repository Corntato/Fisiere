with open("fis_cuv.txt", "r") as f:
    c1 = f.readline().strip()
    c2 = f.readline().strip()
    c3 = f.readline().strip()
    c4 = f.readline().strip()

c_nou = c1[:2] + c2[0] + c3[:3] + c4[:len(c4)//2]

print("Cuvintele citite din fisier sunt:", c1, c2, c3, c4)
print("Cuvântul format este:", c_nou)
