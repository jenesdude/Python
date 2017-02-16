from complex import Complex
from complex_test import ComplexTestCase
import dis

def main():
    print(dis.dis(dis.dis))
    print(dis.dis(ComplexTestCase.testStringRepresentation))


if __name__ == "__main__":
    main()