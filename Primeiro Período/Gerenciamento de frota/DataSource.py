from Vehicle import Vehicle

class DataSource: 
  vehicles = []
  
  def __init__(self) -> None:
    self.loadBase()
  
  def loadBase(self) -> None:
    try:
      dataBase = None

      if not self.fileExists():
        dataBase = open('fleet.csv', 'w', encoding='utf-8')
        dataBase.close()

      dataBase = open('fleet.csv', 'r', encoding='utf-8')
      for line in dataBase.readlines():
        id, name, place, year, brand, color, mileage = line.replace('\n', '').split(";")
        vehicle = Vehicle(id, name, place, year, brand, color, mileage)

        self.vehicles.append({
          "id": vehicle.id,
          "name": vehicle.name,
          "place": vehicle.place,
          "year": vehicle.year,
          "brand": vehicle.brand,
          "color": vehicle.color,
          "mileage": vehicle.mileage,
        })

      dataBase.close()
    except Exception as e:
      print("Erro ao carregar base de dados: ", e)

  def fileExists(self) -> bool:
    try: 
      open('fleet.csv', 'r', encoding='utf-8')
      return True
    except:
      return False
    
  def addVehicle(self, data) -> {"status"}:
    if len([vehicle for vehicle in self.vehicles if vehicle["place"].lower() == data["place"].lower()]):
      raise Exception("Placa já cadastrada")
    
    id = self.implementsId()
    vehicle = Vehicle(id, data["name"], data["place"], data["year"], data["brand"], data["color"], data["mileage"])

    self.vehicles.append({
      "id": vehicle.id,
      "name": vehicle.name,
      "place": vehicle.place,
      "year": vehicle.year,
      "brand": vehicle.brand,
      "color": vehicle.color,
      "mileage": vehicle.mileage,
    })

    return { "status": 1 }

  def editVehicle(self, key, value, data) -> {"status"}:
    index = [index for index, vehicle in enumerate(self.vehicles) if str(vehicle[key]).lower() == value.lower()]
    if not len(index):
      raise Exception("Veículo não encontrado")

    self.vehicles[index[0]] = {
      "id": self.vehicles[index[0]]["id"],
      "name": data["newName"],
      "place": data["newPlace"],
      "year": data["newYear"],
      "brand": data["newBrand"],
      "color": data["newColor"],
      "mileage": data["newMileage"],
    }
    return { "status": 1 }
    
  def implementsId(self) -> int:
    if len(self.vehicles):
      return sorted([i["id"] for i in self.vehicles])[-1] + 1
    else: 
      return 0

  def searchVehicles(self, key, value) -> list:
    vehicles = [vehicle for vehicle in self.vehicles if str(vehicle[key]).lower() == value.lower()]
    if not len(vehicles):
      raise Exception("Veículo não encontrado")
    
    return vehicles

  def deleteVehicle(self, key, value) -> {"status"}:
    index = [index for index, vehicle in enumerate(self.vehicles) if str(vehicle[key]).lower() == value.lower()]
    if not len(index):
      raise Exception("Veículo não encontrado")

    self.vehicles.pop(index[0])
    return { "status": 1 }

  def saveInDataBase(self) -> None:
    try:
      if self.fileExists():
        dataBase = open('fleet.csv', 'w', encoding='utf-8')
        dataBase.truncate()
        dataBase.close()
      
      dataBase = open('fleet.csv', 'a', encoding='utf-8')
      for vehicle in self.vehicles:
        dataBase.write(f"{vehicle['id']};{vehicle['name']};{vehicle['place']};{vehicle['year']};{vehicle['brand']};{vehicle['color']};{vehicle['mileage']}\n")

      dataBase.close()
    except Exception as e:
      print("Erro ao salvar base de dados: ", e)
      