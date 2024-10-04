class Prodotto:
    count = 0

    def __init__(self, nome, quantita, prezzo):
        self.nome = nome
        self.quantita = quantita
        self.prezzo = prezzo
        Prodotto.count += 1

    def valore_totale(self):
        """Calcola il valore totale del prodotto in magazzino."""
        return self.quantita * self.prezzo

    @staticmethod
    def numero_prodotti():
        """Restituisce il numero totale di prodotti creati."""
        return Prodotto.count


def main():
    prodotto1 = Prodotto("Mela", 50, 0.5)  # 50 mele a 0.5 euro ciascuna
    prodotto2 = Prodotto("Banana", 30, 0.3)  # 30 banane a 0.3 euro ciascuna

    print(f"Valore totale di {prodotto1.nome} in magazzino: {prodotto1.valore_totale()} euro")
    print(f"Valore totale di {prodotto2.nome} in magazzino: {prodotto2.valore_totale()} euro")

    print(f"Numero totale di prodotti creati: {Prodotto.numero_prodotti()}")

if __name__ == "__main__":
    main()

