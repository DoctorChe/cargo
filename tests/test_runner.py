import unittest
import test_common
import test_echo
import test_staff
import test_vehicle
import test_load

cargoTestSuite = unittest.TestSuite()
cargoTestSuite.addTest(unittest.makeSuite(test_echo.TestEcho))
cargoTestSuite.addTest(unittest.makeSuite(test_common.TestCargoInstance))
cargoTestSuite.addTest(unittest.makeSuite(test_common.TestProtocolCreateCommand))
cargoTestSuite.addTest(unittest.makeSuite(test_common.TestProtocolCreateResponse))
cargoTestSuite.addTest(unittest.makeSuite(test_common.TestHandler))
cargoTestSuite.addTest(unittest.makeSuite(test_staff.TestStaff))
cargoTestSuite.addTest(unittest.makeSuite(test_vehicle.TestVehicle))
cargoTestSuite.addTest(unittest.makeSuite(test_load.TestLoad))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(cargoTestSuite)
