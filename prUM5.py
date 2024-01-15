
with open("fisier_cuvinte.txt", "r") as f:
    c1 = f.readline().strip()
    c2 = f.readline().strip()
    c3 = f.readline().strip()
    c4 = f.readline().strip()

frază = f"{c1} {c2} {c3} {c4}."

print("Cuvintele citite din fisier sunt:", c1, c2, c3, c4)
print("Fraza formată este:", frază)
