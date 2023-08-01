import pytest
import functions

def test_readStateFile(tmp_path):
    # Create a temporary file with test data
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test data")

    # Call the function with the test file
    result = functions.readStateFile(test_file)

    # Assert that the result is equal to the expected output
    assert result == ["Test data"]

def test_checkOrderByDate():
    # Test case: array is ordered by date
    arrdata = ["item1,1.0,description1", "item2,2.0,description2", "item3,3.0,description3"]
    assert functions.checkOrderByDate(arrdata) == 0

    # Test case: array is not ordered by date
    arrdata = ["item1,3.0,description1", "item2,2.0,description2", "item3,1.0,description3"]
    assert functions.checkOrderByDate(arrdata) == 1

def test_SortByDate():
    # Test case: list is already sorted by date
    strings = ["item1,1.0,description1", "item2,2.0,description2", "item3,3.0,description3"]
    assert functions.SortByDate(strings) == ["item1,1.0,description1", "item2,2.0,description2", "item3,3.0,description3"]

    # Test case: list needs to be sorted by date
    strings = ["item1,3.0,description1", "item2,2.0,description2", "item3,1.0,description3"]
    assert functions.SortByDate(strings) == ["item3,1.0,description3", "item2,2.0,description2", "item1,3.0,description1"]

    # Test case: list is empty
    strings = []
    assert functions.SortByDate(strings) == []

def test_SellWithoutTax():
    #Test case: list is empty
    arrdata = []
    assert functions.SellWithoutTax(arrdata) == 0.0

    #Test case: array with one element, where the time is greater than SEC_IN_YEAR
    arrdata = ["10.0, 1598346000, somedata"]
    assert functions.SellWithoutTax(arrdata) == 10.0

    #Test case: input array with one element, where the time is less than SEC_IN_YEAR
    arrdata = ["10.0, 1698346000, someotherdata"]
    assert functions.SellWithoutTax(arrdata) == 0.0

    #Test case:an input array with multiple elements, where some elements can be sold without tax
    arrdata = ["5.0, 1798346000, data1", "20.0, 1638346000, data2", "15.0, 1645862400, data3"]
    assert functions.SellWithoutTax(arrdata) == 35.0

    #Test case: an input array with multiple elements, where all elements can be sold without tax
    arrdata = ["10.0, 1598346000, data1", "20.0, 1638346000, data2", "15.0, 1645862400, data3"]
    assert functions.SellWithoutTax(arrdata) == 45.0


# Run the test
pytest.main()
