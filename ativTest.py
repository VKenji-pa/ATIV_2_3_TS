class TestCase:
    
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result):
        result.test_started()
        self.set_up()    # chama método de setup
        
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()    # chama método de teste
        except AssertionError as e:
            result.add_failure(self.test_method_name)
        except Exception as e:
            result.add_error(self.test_method_name)
            
        self.tear_down() # chama método de teardown 

    def set_up(self):
        pass

    def tear_down(self):
        pass
    
class TestSuite:
    pass

class TestResult:
    RUN_MSG = "run"
    FAILURE_MSG = "failed"
    ERROR_MSG = "error"
    
    def __init__(self, suite_name=None):
        self.run_count = 0
        self.failures = []
        self.errors = []
        
    def test_started(self):
        self.run_count += 1
    
    def add_failure(self, test):
        self.failures.append(test)
        
    def add_error(self, test):
        self.errors.append(test)
        
    def summary(self):
        return f'{self.run_count} {self.RUN_MSG}, ' \
               f'{str(len(self.failures))} {self.FAILURE_MSG}, ' \
               f'{str(len(self.errors))} {self.ERROR_MSG}'
    

class TestLoader:
    pass

class TestRunner:   
    pass

####### EXEMPLO DE USO ###

class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')
        
class TestStub(TestCase):
    
    def test_success(self):
        assert True
    
    def test_failure(self):
        assert False
    
    def test_error(self):
        raise Exception
    
class TestSpy(TestCase):
    
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.was_run = False
        self.was_set_up = False
        self.was_tear_down = False
        self.log = ""
        
    def set_up(self):
        self.was_set_up = True
        self.log += "set_up "
    
    def test_method(self):
        self.was_run = True
        self.log += "test_method "
        
    def tear_down(self):
        self.was_tear_down = True
        self.log += "tear_down"
    
class TestCaseTest(TestCase):
    
    def set_up(self):
        self.result = TestResult()
        
    def test_result_success_run(self):
        stub = TestStub("test_success")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 0 failed, 0 error"
        
    def test_result_failure_run(self):
        stub = TestStub("test_failure")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 1 failed, 0 error"
    
    def test_result_error_run(self):
        stub = TestStub("test_error")
        stub.run(self.result)
        assert self.result.summary() == "1 run, 0 failed, 1 error"
        
    def test_result_multiple_run(self):
        stub = TestStub("test_success")
        stub.run(self.result)
        stub = TestStub("test_failure")
        stub.run(self.result)
        stub = TestStub("test_error")
        stub.run(self.result)
        
        assert self.result.summary() == "3 run, 1 failed, 1 error"
        
    def test_was_set_up(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.was_set_up
        
    def test_was_run(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.was_run
        
    def test_was_tear_down(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.was_tear_down
    
    def test_template_method(self):
        spy = TestSpy("test_method")
        spy.run(self.result)
        assert spy.log == "set_up test_method tear_down"

# PARTE 2-3
print("Parte 2-3\n")

result = TestResult()
     
test = MyTest('test_a')
test.run(result)

test = MyTest('test_b')
test.run(result)

test = MyTest('test_c')
test.run(result)

print(result.summary())

print("\nParte 4\n")

## PARTE 4

result = TestResult()

test = TestCaseTest('test_result_success_run')
test.run(result)

test = TestCaseTest('test_result_failure_run')
test.run(result)

test = TestCaseTest('test_result_error_run')
test.run(result)

test = TestCaseTest('test_result_multiple_run')
test.run(result)

test = TestCaseTest('test_was_set_up')
test.run(result)

test = TestCaseTest('test_was_run')
test.run(result)

test = TestCaseTest('test_was_tear_down')
test.run(result)

test = TestCaseTest('test_template_method')
test.run(result)

print(result.summary())