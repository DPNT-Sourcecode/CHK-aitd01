from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15

        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAAA") == 300


        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBB") == 75
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBBBB") == 120

        assert checkout_solution.checkout("ADBCBBACCDAA") == 180 + 75 + 3*20 + 2*15 # 4A 3B 3C 2D 

        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout(None) == -1
        assert checkout_solution.checkout("a") == -1
