import unittest

from . import test_common
from . import test_echo
from . import test_staff
from . import test_vehicle
from . import test_load
from . import test_route


if __name__ == '__main__':
    cargoTestSuite = unittest.TestSuite()
    cargoTestSuite.addTest(unittest.makeSuite(test_echo.TestEcho))
    cargoTestSuite.addTest(unittest.makeSuite(test_common.TestCargoInstance))
    cargoTestSuite.addTest(unittest.makeSuite(test_common.TestProtocolCreateCommand))
    cargoTestSuite.addTest(unittest.makeSuite(test_common.TestProtocolCreateResponse))
    cargoTestSuite.addTest(unittest.makeSuite(test_common.TestHandler))
    cargoTestSuite.addTest(unittest.makeSuite(test_staff.TestStaff))
    cargoTestSuite.addTest(unittest.makeSuite(test_vehicle.TestVehicle))
    cargoTestSuite.addTest(unittest.makeSuite(test_load.TestLoad))
    cargoTestSuite.addTest(unittest.makeSuite(test_route.TestCity))
    cargoTestSuite.addTest(unittest.makeSuite(test_route.TestWarehouse))
    cargoTestSuite.addTest(unittest.makeSuite(test_route.TestRoute))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(cargoTestSuite)
