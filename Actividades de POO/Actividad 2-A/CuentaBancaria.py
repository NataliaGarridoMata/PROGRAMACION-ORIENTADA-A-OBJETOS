class CuentaBancaria:
  def __init__(self,titular,numeroCuenta,saldo):
      self.titular=titular
      self.numeroCuenta=numeroCuenta
      self.saldo=saldo
      
  def depositar(self,cantidad):
     self.saldo = self.saldo + cantidad  
     print(f"Se depositaron {cantidad}. Saldo actual: {self.saldo}")
      
  def retirar(self,cantidad):
      if cantidad <= self.saldo:
         self.saldo = self.saldo - cantidad  
       
      else:
          print(f"Se retiraron {cantidad}. Saldo actual: {self.saldo}")
          print("Fondos insuficientes")
  def consultarSaldo(self):
      return self.saldo
  
  def mostrarInformacion(self):
      return f"{self.titular} tienes {self.saldo}"


cuenta1=CuentaBancaria ("Antonio", "11140603", 1000) 
print(cuenta1.mostrarInformacion())  
cuenta1.depositar(500.0)         
cuenta1.retirar(2000.0)
cuenta1.depositar(300.0)
print(cuenta1.mostrarInformacion())

