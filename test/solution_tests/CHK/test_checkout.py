from solutions.CHK import checkout_solution
from solutions.CHK import products

class TestCheckout():
    def test_checkout(self):
        # assert checkout_solution.checkout("A") == 50
        # assert checkout_solution.checkout("B") == 30
        # assert checkout_solution.checkout("C") == 20
        # assert checkout_solution.checkout("D") == 15
        # assert checkout_solution.checkout("E") == 40
        # assert checkout_solution.checkout("F") == 10

        # assert checkout_solution.checkout("AA") == 100
        # assert checkout_solution.checkout("AAA") == 130
        # assert checkout_solution.checkout("AAAAA") == 200
        # assert checkout_solution.checkout("AAAAAAA") == 300
        # assert checkout_solution.checkout("AAAAAAAA") == 330
        # assert checkout_solution.checkout("AAAAAAAAA") == 380
        # assert checkout_solution.checkout("AAAAAAAAAA") == 400
        # assert checkout_solution.checkout("AAAAAAAAAAAA") == 500 # 12A
        # assert checkout_solution.checkout("AAAAAAAAAAAAA") == 530 # 13A


        # assert checkout_solution.checkout("BB") == 45
        # assert checkout_solution.checkout("BBB") == 75
        # assert checkout_solution.checkout("BBBB") == 90
        # assert checkout_solution.checkout("BBBBB") == 120

        # assert checkout_solution.checkout("EE") == 80
        # assert checkout_solution.checkout("EEB") == 80
        # assert checkout_solution.checkout("EEBB") == 110
        # assert checkout_solution.checkout("EEBBB") == 125
        # assert checkout_solution.checkout("EEEEB") == 160
        # assert checkout_solution.checkout("EEEEBB") == 160

        # assert checkout_solution.checkout("FF") == 20
        # assert checkout_solution.checkout("FFF") == 20
        # assert checkout_solution.checkout("FFFF") == 30
        # assert checkout_solution.checkout("FFFFF") == 40


        # assert checkout_solution.checkout("ADBCBBACCDAA") == 180 + 75 + 3*20 + 2*15 # 4A 3B 3C 2D 
        # assert checkout_solution.checkout("FFADBCBBFACFCDAA") == 180 + 75 + 3*20 + 2*15 + 30 # 4A 3B 3C 2D 4F

        assert checkout_solution.checkout("STX") == 45
        assert checkout_solution.checkout("TXY") == 45
        assert checkout_solution.checkout("XYZ") == 45
        assert checkout_solution.checkout("XYZTXY") == 90
        assert checkout_solution.checkout("XXX") == 45

        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout(None) == -1
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("ADBCBBaACxCDAA") == -1


    def test_checkout_from_server(self):
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("G") == 20
        assert checkout_solution.checkout("H") == 10
        assert checkout_solution.checkout("I") == 35
        assert checkout_solution.checkout("J") == 60
        assert checkout_solution.checkout("K") == 70
        assert checkout_solution.checkout("L") == 90
        assert checkout_solution.checkout("M") == 15
        assert checkout_solution.checkout("N") == 40
        assert checkout_solution.checkout("O") == 10
        assert checkout_solution.checkout("P") == 50
        assert checkout_solution.checkout("Q") == 30
        assert checkout_solution.checkout("R") == 50
        assert checkout_solution.checkout("S") == 20
        assert checkout_solution.checkout("T") == 20
        assert checkout_solution.checkout("U") == 40
        assert checkout_solution.checkout("V") == 50
        assert checkout_solution.checkout("W") == 20
        assert checkout_solution.checkout("X") == 17
        assert checkout_solution.checkout("Y") == 20
        assert checkout_solution.checkout("Z") == 21
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("-") == -1
        assert checkout_solution.checkout("ABCa") == -1
        assert checkout_solution.checkout("AxA") == -1
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVW") == 795
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        assert checkout_solution.checkout("AAAAAAAAAA") == 400
        assert checkout_solution.checkout("P") == 50
        assert checkout_solution.checkout("PP") == 100
        assert checkout_solution.checkout("PPP") == 150
        assert checkout_solution.checkout("PPPP") == 200
        assert checkout_solution.checkout("PPPPP") == 200
        assert checkout_solution.checkout("PPPPPP") == 250
        assert checkout_solution.checkout("PPPPPPP") == 300
        assert checkout_solution.checkout("PPPPPPPP") == 350
        assert checkout_solution.checkout("PPPPPPPPP") == 400
        assert checkout_solution.checkout("PPPPPPPPPP") == 400
        assert checkout_solution.checkout("UUU") == 120
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("UUUUU") == 160
        assert checkout_solution.checkout("UUUUUUUU") == 240
        assert checkout_solution.checkout("UUUUUUUU") == 240
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEEB") == 120
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("BEBEEE") == 160
        assert checkout_solution.checkout("RRR") == 150
        assert checkout_solution.checkout("RRRQ") == 150
        assert checkout_solution.checkout("RRRRQ") == 200
        assert checkout_solution.checkout("RRRRRRQQ") == 300
        assert checkout_solution.checkout("RRRQRQRR") == 300
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("H") == 10
        assert checkout_solution.checkout("HH") == 20
        assert checkout_solution.checkout("HHH") == 30
        assert checkout_solution.checkout("HHHH") == 40
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHH") == 55
        assert checkout_solution.checkout("HHHHHHH") == 65
        assert checkout_solution.checkout("HHHHHHHH") == 75
        assert checkout_solution.checkout("HHHHHHHHH") == 85
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("HHHHHHHHHHH") == 90
        assert checkout_solution.checkout("HHHHHHHHHHHH") == 100
        assert checkout_solution.checkout("HHHHHHHHHHHHH") == 110
        assert checkout_solution.checkout("HHHHHHHHHHHHHH") == 120
        assert checkout_solution.checkout("HHHHHHHHHHHHHHH") == 125
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHH") == 135
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHHH") == 145
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHHHH") == 155
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHHHHH") == 165
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHHHHHH") == 160
        assert checkout_solution.checkout("K") == 70
        assert checkout_solution.checkout("KK") == 120
        assert checkout_solution.checkout("KKK") == 190
        assert checkout_solution.checkout("KKKK") == 240
        assert checkout_solution.checkout("V") == 50
        assert checkout_solution.checkout("VV") == 90
        assert checkout_solution.checkout("VVV") == 130
        assert checkout_solution.checkout("VVVV") == 180
        assert checkout_solution.checkout("VVVVV") == 220
        assert checkout_solution.checkout("VVVVVV") == 260
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBB") == 75
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("NNN") == 120
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("NNNNM") == 160
        assert checkout_solution.checkout("NNNNNNMM") == 240
        assert checkout_solution.checkout("NNNMNMNN") == 240
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("Q") == 30
        assert checkout_solution.checkout("QQ") == 60
        assert checkout_solution.checkout("QQQ") == 80
        assert checkout_solution.checkout("QQQQ") == 110
        assert checkout_solution.checkout("QQQQQ") == 140
        assert checkout_solution.checkout("QQQQQQ") == 160
        assert checkout_solution.checkout("V") == 50
        assert checkout_solution.checkout("VV") == 90
        assert checkout_solution.checkout("VVV") == 130
        assert checkout_solution.checkout("VVVV") == 180
        assert checkout_solution.checkout("H") == 10
        assert checkout_solution.checkout("HH") == 20
        assert checkout_solution.checkout("HHH") == 30
        assert checkout_solution.checkout("HHHH") == 40
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHH") == 55
        assert checkout_solution.checkout("HHHHHHH") == 65
        assert checkout_solution.checkout("HHHHHHHH") == 75
        assert checkout_solution.checkout("HHHHHHHHH") == 85
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("STX") == 45
        assert checkout_solution.checkout("STXSTX") == 90
        assert checkout_solution.checkout("SSS") == 45
        assert checkout_solution.checkout("SSSZ") == 65
        assert checkout_solution.checkout("ZZZ") == 45
        assert checkout_solution.checkout("ZZZS") == 65
        assert checkout_solution.checkout("STXS") == 62
        assert checkout_solution.checkout("STXZ") == 62
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1602
        assert checkout_solution.checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH") == 1602
        assert checkout_solution.checkout("AAAAAPPPPPUUUUEEBRRRQAAAHHHHHHHHHHKKVVVBBNNNMFFFQQQVVHHHHHSTX") == 1655
        assert checkout_solution.checkout("CXYZYZC") == 122
# 2C  2Z 2Y X
# 2*20    + 2*21 + 2*20 + 17 = 122 not 127 ?
# 2c x 2y 2z