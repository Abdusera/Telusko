class HAMAD :
    def __init__(self,Baba,Mama):
        self.Baba = Baba
        self.Mama = Mama
    def family(self):
        print("HUYU ANAITWA ANAITWA ",self.Baba,end="")
        print(" NA MAMA YAKE ANAITWA ",  self.Mama)
Dada1 = HAMAD("SALMA HAMAD ALI","HUSNA")
Dada2 = HAMAD("ZUBYDA HAMAD ALI ","HUSNA")
Dada1.family()
Dada2.family()