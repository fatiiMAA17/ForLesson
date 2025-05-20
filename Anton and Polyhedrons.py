n = int(input()); k = 0; Tetrahedron = 4; Cube = 6; Octahedron = 8; Dodecahedron = 12; Icosahedron = 20
for _ in range(n):
  figure = input()
  if figure == "Tetrahedron":
    k += Tetrahedron
  elif figure == "Cube":
    k += Cube
  elif figure == "Octahedron":
    k += Octahedron
  elif figure == "Dodecahedron":
    k += Dodecahedron
  elif figure == "Icosahedron":
    k += Icosahedron
print(k)