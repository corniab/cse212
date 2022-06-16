from doubly_linked import Doubly_Linked

class Test_Doubly_Linked:

    def test_str(self):
        case = Doubly_Linked()
        case.append(1)
        case.append(2)
        case.append(3)
        case.append(4)
        result = "HEAD -> 1 -> 2 -> 3 -> 4 <- TAIL"

        try:
            str(case) == result
            print(f"PASSED: {str.__name__}({case}) == {result}")
        except AssertionError:
            print(f"FAILED: {str.__name__}({case}) == {result}")

    def test_append(self):
        case = Doubly_Linked()

        result = "HEAD -> 1 <- TAIL"

        try:
            str(case.append(1)) == result
            print(f"PASSED: linkedList.append(1)")
        except AssertionError:
            print(f"FAILED: linkedList.append(1)")

dl = Test_Doubly_Linked()

dl.test_str()