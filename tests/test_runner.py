import unittest
import test_echo
import test_common

cargoTestSuite = unittest.TestSuite()
cargoTestSuite.addTest(unittest.makeSuite(test_echo.TestEcho))
cargoTestSuite.addTest(unittest.makeSuite(test_common.TestCargoInstance))
cargoTestSuite.addTest(unittest.makeSuite(test_common.TestProtocolCreateCommand))
cargoTestSuite.addTest(unittest.makeSuite(test_common.TestProtocolCreateResponse))
cargoTestSuite.addTest(unittest.makeSuite(test_common.TestHandler))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(cargoTestSuite)
