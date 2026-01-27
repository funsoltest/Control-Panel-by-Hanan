import pytest
from main.driver_manager import DriverManager

@pytest.fixture(scope="session")
def driver():
    print("Launching App")
    manager = DriverManager()
    driver = manager.start_driver()

    yield driver
    print(" Closing App")
    driver.quit()

