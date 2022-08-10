import subprocess
from base_class import *
from time import sleep


class my_sample_test(BaseClass):
    """
    Sample working TestCase with One TestCase
    """

    def __init__(self):
        super().__init__()
        
    @BaseClass.setup
    def my_setup(self):
        self.logger.info("print from my setup")
        return True

    @BaseClass.test(tags=[["sanity_tc1"]])
    def test_case_1(self):
        self.logger.info("print from TestCase1")
        print(subprocess.Popen('pwd', shell=True))
        print(subprocess.Popen('cd ../../customer_code; ls', shell=True))
        subprocess.Popen('cd ../../customer_code; make', shell=True)
        subprocess.Popen('cd ../../customer_code; makemake clean', shell=True)
    
        sleep(0.25)
        return (True)
    @BaseClass.teardown
    def my_teardown(self):
        self.logger.infot("from teardown")
