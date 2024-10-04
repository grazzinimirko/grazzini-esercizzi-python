class Calcolatrice:
    @staticmethod
    def somma(a, b):
        """Restituisce la somma di a e b."""
        return a + b

    @staticmethod
    def sottrazione(a, b):
        """Restituisce la sottrazione di b da a."""
        return a - b

    @staticmethod
    def moltiplicazione(a, b):
        """Restituisce il prodotto di a e b."""
        return a * b

    @staticmethod
    def divisione(a, b):
        """Restituisce la divisione di a per b. Solleva un'eccezione se b è zero."""
        if b == 0:
            raise ValueError("Errore: Divisione per zero non consentita.")
        return a / b



def main():
   
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

  
    print(f"{num1} + {num2} = {Calcolatrice.somma(num1, num2)}")
    print(f"{num1} - {num2} = {Calcolatrice.sottrazione(num1, num2)}")
    print(f"{num1} * {num2} = {Calcolatrice.moltiplicazione(num1, num2)}")
    
    try:
        print(f"{num1} / {num2} = {Calcolatrice.divisione(num1, num2)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

