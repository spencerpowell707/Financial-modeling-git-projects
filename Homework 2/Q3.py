


def FullPrice(Freq, YTM, Face, Coupon, Period ):
    PVcf = 0
    for i in range (Period + 1):
        PVcf += Coupon / (1+ YTM/Freq)**(i) 
    Fprice = PVcf + Face / (1 + YTM/Freq)**(Period)
    return Fprice


def Main():
    
    Freq = 2
    YTM = .12
    Face = 1000
    Coupon = 10
    Period = 40
    Full_Price = FullPrice(Freq, YTM, Face, Coupon, Period)
    
    print('Full Price:' .ljust(20), "$", round(Full_Price, 4))