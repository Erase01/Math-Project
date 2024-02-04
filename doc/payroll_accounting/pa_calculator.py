class pa_calculator:            # pa = payroll accounting
    def __init__(self, einkommen, kinderfreibetrag=0):
        self.einkommen = einkommen
        self.kinderfreibetrag = kinderfreibetrag

    def percent(self, p):
        return p / 100

    def berechung_zu_versteuerndes_einkommen(self):
        basic_allowance = 11.604
        zu_versteuerndes_einkommen = self.einkommen - basic_allowance
        zu_versteuerndes_einkommen -= self.kinderfreibetrag * 6.384
        return max(0, zu_versteuerndes_einkommen)
    
    def lohnsteuer(self):
        zu_versteuerndes_einkommen = self.berechung_zu_versteuerndes_einkommen()
        LSt = zu_versteuerndes_einkommen * self.percent(42)
        return max(0, round(LSt, 2))
    
    def kirchensteuer(self):
        zu_versteuerndes_einkommen = self.berechung_zu_versteuerndes_einkommen()
        KSt = zu_versteuerndes_einkommen * self.percent(9)
        return max(0, round(KSt, 2))
    
    def solidaritaetszuschlag(self):
        zu_versteuerndes_einkommen = self.berechung_zu_versteuerndes_einkommen()
        Soli = zu_versteuerndes_einkommen * self.percent(5.5)
        return max(0, round(Soli, 2))
    
    def sv(self):
        KV = 7.3
        RV = 9.3
        AV = 1.3
        PV = 1.7
        SV = KV + RV + AV + PV
        cal = 5175  # Contribution assessment limit
        zu_versteuerndes_einkommen = self.berechung_zu_versteuerndes_einkommen()

        if zu_versteuerndes_einkommen <= cal:
            SV = zu_versteuerndes_einkommen - zu_versteuerndes_einkommen * self.percent(SV)
            return max(0, round(SV, 2))
        else:
            SV = cal - cal * self.percent(SV)
            return max(0, round(SV, 2))
        

if __name__ == '__main__':
    
    einkommen = int(input("Einkommen: "))
    kinderfreibetrag = int(input("Kinderfreibetrag (default=0): "))

    pa = pa_calculator(einkommen, kinderfreibetrag)
    print("Lohnsteuer:", pa.lohnsteuer(), "€")
    print("Kirchensteuer:", pa.kirchensteuer(), "€")
    print("Solidaritätszuschlag:", pa.solidaritaetszuschlag(), "€")
    print("Sozialversicherung:", pa.sv(), "€")
    #print("Nettoeinkommen:", einkommen - pa.lohnsteuer() - pa.kirchensteuer() - pa.solidaritaetszuschlag() - pa.sv(), "€")                 # in progress
    #print("Nettoeinkommen ohne Kirchensteuer:", einkommen - pa.lohnsteuer() - pa.solidaritaetszuschlag() - pa.sv(), "€")