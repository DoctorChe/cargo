import unittest

import test_common
import test_echo
import test_staff
import test_vehicle
import test_load
import test_route


if __name__ == '__main__':
    cargoTestSuite = unittest.TestSuite()
    cargoTestSuite.addTest(unittest.makeSuite(test_echo.TestEcho))
    cargoTestSuite.addTest(unittest.makeSuite(test_common.TestCargoInstance))
    cargoTestSuite.addTest(unittest.makeSuite(test_common.TestProtocolCreateCommand))
    cargoTestSuite.addTest(unittest.makeSuite(test_common.TestProtocolCreateResponse))
    # cargoTestSuite.addTest(unittest.makeSuite(test_common.TestHandler))
    cargoTestSuite.addTest(unittest.makeSuite(test_staff.TestStaff))
    cargoTestSuite.addTest(unittest.makeSuite(test_vehicle.TestVehicle))
    cargoTestSuite.addTest(unittest.makeSuite(test_load.TestLoad))
    cargoTestSuite.addTest(unittest.makeSuite(test_route.TestCity))
    cargoTestSuite.addTest(unittest.makeSuite(test_route.TestWarehouse))
    cargoTestSuite.addTest(unittest.makeSuite(test_route.TestRoute))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(cargoTestSuite)
