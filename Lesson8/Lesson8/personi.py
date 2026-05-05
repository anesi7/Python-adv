class Personi:

    def __init__(self,emri,vitiilindjes,gjinia):
        self.emri=emri
        self.vitiilindjes=vitiilindjes
        self.gjinia=gjinia

    def prezantimi(self):
        print(f"une jam:{self.emri},kam lindur ne vitin:{self.vitiilindjes}")

    def sayHi(self):
        print(f"pershendetje nga:{self.emri}")
