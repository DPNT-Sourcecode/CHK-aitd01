from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10

        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        assert checkout_solution.checkout("AAAAAAAAAA") == 400
        assert checkout_solution.checkout("AAAAAAAAAAAA") == 500 # 12A
        assert checkout_solution.checkout("AAAAAAAAAAAAA") == 530 # 13A


        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBB") == 75
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBBBB") == 120

        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEBB") == 110
        assert checkout_solution.checkout("EEBBB") == 125
        assert checkout_solution.checkout("EEEEB") == 160
        assert checkout_solution.checkout("EEEEBB") == 160

        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40


        assert checkout_solution.checkout("ADBCBBACCDAA") == 180 + 75 + 3*20 + 2*15 # 4A 3B 3C 2D 
        assert checkout_solution.checkout("FFADBCBBFACFCDAA") == 180 + 75 + 3*20 + 2*15 + 30 # 4A 3B 3C 2D 4F 

        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout(None) == -1
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("ADBCBBaACxCDAA") == -1




