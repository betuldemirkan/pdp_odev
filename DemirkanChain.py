from hashlib import sha256

class block:
    def __init__(self,data,previousHash = ' '):
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hesapla()

    def hesapla(self):
        while True:
            ozet = sha256((str(self.data)+str(self.previousHash)).encode()).hexdigest()
            if ozet[0:2] == "00":
                break
            return ozet

class blockChain:
    def __init__(self):
        self.chain = [self.genesisOlustur()]

    def genesisOlustur(self):
        return block("Demirkan"," ")

    def blockEkle(self,data):
        node = block(data,self.chain[-1].hash)
        self.chain.append(node)

    def kontrol(self):
        for i in range(len(self.chain)):
            if i != 0:
                ilk = self.chain[i-1].hash
                suan = self.chain[i].previousHash
                if ilk != suan:
                    return "Zincir kopmuş"
                if sha256((str(self.chain[i].data)+str(self.chain[i].previousHash)).encode()).hexdigest() != self.chain[i].hash:
                    return "Zincir kopmuş"
            return "Sağlam"

    def listeleme(self):
        print("\nBlockchain")
        for i in range(len(self.chain)):
            print("------------------------------")
            print("Block => ",i,"\nHash = ",str(self.chain[i].hash),"\nData = ",str(self.chain[i].data),"\nPreviousHash = ",str(self.chain[i].previousHash))
            print("------------------------------")

DemirkanCoin = blockChain()
while True:
    print("Lütfen seçimlerinizi yapın \nBlock eklemek için 1 \nBlockchaini görmek için 2 \nZinciri kontrol etmek için 3\nÇıkmak inin 4'ü seçiniz")
    data=input("Seçim: ")
    if data == "1":
        miktar = input("\nGönderilen miktarı giriniz: ")
        DemirkanCoin.blockEkle(miktar)
    elif data == "2":
        DemirkanCoin.listeleme()
    elif data == "3":
        print(str(DemirkanCoin.kontrol()))
    elif data == "4":
        break