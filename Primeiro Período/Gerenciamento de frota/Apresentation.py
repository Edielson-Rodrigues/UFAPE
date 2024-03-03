from DataSource import DataSource

class Apresentation:
  initialization = True
  def __init__(self) -> None:
    self.dataSource = DataSource()
    self.searchParams = {1: "id", 2: "place", 3: "name", 4: "brand", 5: "color", 6: "year", 7: "mileage"}

  def rendererMenu(self) -> any:
    self.showMesage(self.initialization)
    try:
      option = int(input("\nDigite a opção desejada: "))

      match option:
        case 1: 
          return self.viewAllVehicles()
        case 2:
          return self.addVehicle()
        case 3:
          return self.deleteVehicle()
        case 4:
          return self.editVehicle()
        case 5: 
          return self.viewEspeficsVehicles()
        case 0:
          print("\nAté mais!\n")
        case _:
          print("\nOpção inválida\n")
          return self.rendererMenu()
      
      return self.dataSource.saveInDataBase()
    
    except Exception as e:
      print("Erro ao ler opção: ", e, "\n")
      self.rendererMenu()

  def showMesage(self, showWelcome) -> None:
    if showWelcome:
      print("-"*12 + "Bem-vindo ao sistema de gerenciamento de frotas" + "-"*12)
      self.initialization = False
          
    print("1 - Visualizar todos os veículos da frota")
    print("2 - Adicionar um veículo à frota")
    print("3 - Remover um veículo da frota")
    print("4 - Editar um veículo da frota")
    print("5 - Buscar veículo/os por atributos")

  def showVehicles(self, vehicles) -> None:
    for vehicle in vehicles:
      print(f"id: {vehicle['id']}")
      print(f"Nome: {vehicle['name']}")
      print(f"Placa: {vehicle['place']}")
      print(f"Ano: {vehicle['year']}")
      print(f"Marca: {vehicle['brand']}")
      print(f"Cor: {vehicle['color']}")
      print(f"Quilometragem: {vehicle['mileage']}")
      print("-"*24, "\n")

  def viewAllVehicles(self) -> None:
    
    if len(self.dataSource.vehicles):
      print("\n", "-"*12 + "Veículos cadastrados" + "-"*12, "\n")
      self.showVehicles(self.dataSource.vehicles)
    else: 
      print("\nNenhum veículo cadastrado\n")
    
    self.rendererMenu()

  def addVehicle(self) -> None:
    try:
      data = {}
      data["name"] = input("\nDigite o nome do veículo: ")
      data["place"] = input("Digite a placa do veículo: ")
      data["year"] = input("Digite o ano do veículo: ")
      data["brand"] = input("Digite a marca do veículo: ")
      data["color"] = input("Digite a cor do veículo: ")
      data["mileage"] = input("Digite a quilometragem do veículo: ")
      result = self.dataSource.addVehicle(data)

      if result["status"] == 1:
        print("Veículo adicionado com sucesso!")
      print()

      self.rendererMenu()
    except Exception as e:
      print("Erro ao adicionar veículo: ", e, "\n")
      self.rendererMenu()
  
  def viewEspeficsVehicles(self) -> None:
    try:
      print("\n", "-"*12 + "Buscar veículos por atributos" + "-"*12, "\n")
      print("1 - Buscar por id")
      print("2 - Buscar por placa")
      print("3 - Buscar por nome")
      print("4 - Buscar por marca")
      print("5 - Buscar por cor")
      print("6 - Buscar por ano")
      print("7 - Buscar por quilometragem")

      option = int(input("\nDigite a opção desejada: "))      
      value = input("Digite o valor: ")

      vehicles = self.dataSource.searchVehicles(self.searchParams[option], value)

      print("\n", "-"*12 + "Veículos encontrados" + "-"*12, "\n")
      self.showVehicles(vehicles)
      self.rendererMenu()
    
    except Exception as e:
      print("Erro ao buscar veículo: ", e, "\n")
      self.rendererMenu() 
  
  def editVehicle(self) -> None:
    try: 
      print("1 - Editar por id")
      print("2 - Editar por placa")

      option = int(input("\nDigite a opção desejada: "))

      if option == 1 or option == 2:
        value = input("Digite o valor: ")
        vehicle = self.dataSource.searchVehicles(self.searchParams[option], value)

        print("\n", "-"*12 + "Veículo encontrado" + "-"*12, "\n")
        self.showVehicles(vehicle)

        data = {}
        data["newName"] = input("Digite o novo nome: ")
        data["newPlace"] = input("Digite a nova placa: ")
        data["newYear"] = input("Digite o novo ano: ")
        data["newBrand"] = input("Digite a nova marca: ")
        data["newColor"] = input("Digite a nova cor: ")
        data["newMileage"] = input("Digite a nova quilometragem: ")

        result = self.dataSource.editVehicle(self.searchParams[option], value, data)
        if result["status"] == 1:
          print("Veículo editado com sucesso!\n")
          self.rendererMenu()
      else:
        raise Exception("Opção inválida")
    
    except Exception as e:
      print("Erro ao editar veículo: ", e, "\n")
      self.rendererMenu()    
  
  def deleteVehicle(self) -> None:
    try: 
      print("1 - Deletar por id")
      print("2 - Deletar por placa")

      option = int(input("\nDigite a opção desejada: "))

      if option == 1 or option == 2:
        value = input("Digite o valor: ")
        vehicle = self.dataSource.searchVehicles(self.searchParams[option], value)

        print("\n", "-"*12 + "Veículo encontrado" + "-"*12, "\n")
        self.showVehicles(vehicle)

        result = self.dataSource.deleteVehicle(self.searchParams[option], value)
        if result["status"] == 1:
          print("Veículo deletado com sucesso!\n")
          self.rendererMenu()
      else:
        raise Exception("Opção inválida")
      
    except Exception as e:
      print("Erro ao deletar veículo: ", e, "\n")
      self.rendererMenu()