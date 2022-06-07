from solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15

        assert checkout_solution.checkout("A A") == 100
        assert checkout_solution.checkout("A A A") == 130
        assert checkout_solution.checkout("A A A A A") == 230
        assert checkout_solution.checkout("A A A A A A A") == 310

