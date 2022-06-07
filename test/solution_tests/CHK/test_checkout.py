from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15

        assert checkout_solution.checkout("A A") == 100
        assert checkout_solution.checkout("A A A") == 130
        assert checkout_solution.checkout("A A A A A") == 230
        assert checkout_solution.checkout("A A A A A A A") == 310


        assert checkout_solution.checkout("B B") == 45
        assert checkout_solution.checkout("B B B") == 75
        assert checkout_solution.checkout("B B B B") == 90
        assert checkout_solution.checkout("B B B B B") == 120

        assert checkout_solution.checkout("A D B C B B A C C D A A") == 180 + 75 + 3*20 + 2*15 # 4A 3B 3C 2D 

