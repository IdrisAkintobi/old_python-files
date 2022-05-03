##########################################################
# Using pickle to serializing and de-serializing python object structure
import pickle


class Area:
    """This is an information gathering program for the community."""

    def __init__(self, name, street, level):
        super(Area, self).__init__()
        self.name = name
        self.street = street
        self.level = level

    def __repr__(self):
        return f"{self.name} is from {self.street} street and a {self.level} member of the Dev team."


jare = Area("Adejare", "Osun", "Professional")

with open("Jare", "wb") as file:
    pickle.dump(jare, file)
with open("Jare", "rb") as file:
    clean = pickle.load(file)
    print(clean)
print(jare.__doc__)
