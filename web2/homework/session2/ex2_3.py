from mongoengine import Document, StringField, IntField
import mlab

mlab.connect()

class river(Document):
    name = StringField()
    continent = StringField()
    length = StringField()

rivers = river.objects()
r_african = []
r_american = []
for r in rivers:
    if r.continent == 'Africa':
        r_african.append(r.name)
        
    if r.continent == 'S. America' and r.length < 1000:
        r_american.append(r.name)

print("RIVER IN AFRICA:")
for i in r_african:
    print(i)

print("\nRIVER IN AMERICA (less than 1000km): ")
for i in r_american:
    print(i)