#!/opt/local/bin/python3.3
def chase(a1_speed, t2_speed, advantage):
    return a1_speed * advantage / (a1_speed - t2_speed)


if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(chase(6, 3, 2), 4, 8), "example"
    assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"
