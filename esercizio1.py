class Studente:
  count=0
  def __init__(self, nome, eta, matricola)
    self.nome = nome
    self.eta = eta
    self.matricola = matricola
    Studente.count += 1
  def visualizza_info(self):
       return f"Nome: {self.nome}, Età: {self.eta}, Matricola: {self.matricola}"

    @staticmethod
    def numero_studenti():
        return Studente.count
studente1 = Studente("Marco Rossi", 20, "12345")
studente2 = Studente("Giulia Verdi", 22, "67890")print(studente1.visualizza_info())
print(studente2.visualizza_info())print(f"Numero totale di studenti: {Studente.numero_studenti()}")
