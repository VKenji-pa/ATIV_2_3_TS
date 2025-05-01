from testFrame import *

result = TestResult()
loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)
suite.run(result)
print("Loader:\n", result.summary(), "\n")

## RUNNER
print("Runner:")

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)
