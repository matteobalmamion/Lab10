from database.DAO import DAO

countries=DAO.getCountries()
print(len(countries))

borders=DAO.getBorders(2000)
count=[]
for border in borders:
    count.extend(borders[border])
print(len(count))