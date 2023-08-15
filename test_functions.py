import pytest
import functions
import time

def test_readStateFile(tmp_path):
    # Create a temporary file with test data
    test_file = tmp_path / "test.txt"
    test_file.write_text("amount,data,price")

    # Call the function with the test file
    arrdata = functions.readStateFile(test_file)
    result  = arrdata[0].price
    # Assert that the result is equal to the expected output
    assert result == "price"

def test_checkOrderByDate(tmp_path):
    # Test case: array is ordered by date
    test_file = tmp_path / "test.txt"
    test_file.write_text("item1,1.0,description1,"
                         "item2,2.0,description2,"
                         "item3,3.0,description3")

    arrdata = functions.readStateFile(test_file)
    assert functions.checkOrderByDate(arrdata) == True

    # Test case: array is not ordered by date
    test_file = tmp_path / "test_2.txt"
    test_file.write_text("item1,10.0,description1,\n"
                         "item2,3.0,description2,\n"
                         "item3,1.0,description3")

    arrdata = functions.readStateFile(test_file)
    assert functions.checkOrderByDate(arrdata) == False

def test_SortByDate(tmp_path):
    # Test case: list is already sorted by date
    test_file = tmp_path / "test_3.txt"
    test_file.write_text("item1,1.0,description1,\n"
                         "item2,2.0,description2,\n"
                         "item3,3.0,description3")

    arrdata = functions.readStateFile(test_file)
    assert functions.SortByDate(arrdata)[0].data == arrdata[0].data
    assert functions.SortByDate(arrdata)[1].data == arrdata[1].data
    assert functions.SortByDate(arrdata)[2].data == arrdata[2].data

    # Test case: list needs to be sorted by date
    test_file = tmp_path / "test_4.txt"
    test_file.write_text("item1,3.0,description1,\n"
                         "item2,2.0,description2,\n"
                         "item3,1.0,description3")

    arrdata_2 = functions.readStateFile(test_file)
    assert functions.SortByDate(arrdata_2)[0].data == arrdata[0].data
    assert functions.SortByDate(arrdata_2)[1].data == arrdata[1].data
    assert functions.SortByDate(arrdata_2)[2].data == arrdata[2].data

    # Test case: list is empty
    arrdata = []
    assert functions.SortByDate(arrdata) == []

def test_SellWithoutTax():
    #Test case: list is empty
    arrdata = []
    assert functions.SellWithoutTax(arrdata, 100) == 0.0

    #Test case: array with one element, where the time is greater than SEC_IN_YEAR
    arrdata = []
    arrline = functions.Record()
    arrline.quantity = '10.0'
    arrline.data = str(time.time() - functions.SEC_IN_YEAR*2)
    arrline.price = '1000'
    arrdata.append(arrline)
    assert functions.SellWithoutTax(arrdata, 1000) == 10.0

    #Test case: input array with one element, where the time is less than SEC_IN_YEAR and price is smaller than now
    arrdata = []
    arrline = functions.Record()
    arrline.quantity = '10.0'
    arrline.data = str(time.time() - 2.0)
    arrline.price = '1000'
    arrdata.append(arrline)
    assert functions.SellWithoutTax(arrdata, 2000) == 0.0

    #Test case: input array with one element, where the time is less than SEC_IN_YEAR but price is bigger than now
    arrdata = []
    arrline = functions.Record()
    arrline.quantity = '10.0'
    arrline.data = str(time.time() - 2.0)
    arrline.price = '1000'
    arrdata.append(arrline)
    assert functions.SellWithoutTax(arrdata, 500) == 10.0

    #Test case:an input array with multiple elements, where some elements can be sold without tax
    arrdata = []
    arrline = functions.Record()
    arrline2 = functions.Record()
    arrline3 = functions.Record()
    arrline.quantity = '1.0'
    arrline.data = str(time.time() - functions.SEC_IN_YEAR*2)
    arrline.price = '1000'
    arrdata.append(arrline)
    arrline2.quantity = '1.0'
    arrline2.data = str(time.time() - functions.SEC_IN_YEAR*2)
    arrline2.price = '3000'
    arrdata.append(arrline2)
    arrline3.quantity = '1.0'
    arrline3.data = str(time.time())
    arrline3.price = '500'
    arrdata.append(arrline3)

    assert functions.SellWithoutTax(arrdata,2000) == 2.0

    #Test case: an input array with multiple elements, where all elements can be sold without tax
    arrdata = []
    arrline = functions.Record()
    arrline2 = functions.Record()
    arrline3 = functions.Record()
    arrline.quantity = '5.0'
    arrline.data = str(time.time() - 2.0)
    arrline.price = '100'
    arrdata.append(arrline)
    arrline2.quantity = '10.0'
    arrline2.data = str(time.time() - 1.0)
    arrline2.price = '100'
    arrdata.append(arrline2)
    arrline3.quantity = '30.0'
    arrline3.data = str(time.time())
    arrline3.price = '500'
    arrdata.append(arrline3)

    assert functions.SellWithoutTax(arrdata, 2) == 45.0

def test_Benefit():
    #Testb case: list is empty
    arrdata = []
    assert functions.Benefit(5, 10, arrdata) == 0

    #Test case: one line of data, sum is smaller than arrline[0]
    arrdata = []
    arrline = functions.Record()
    arrline.quantity = '10.0'
    arrline.data = '1234567890'
    arrline.price = '0.5'
    arrdata.append(arrline)
    sum = 5
    price = 10
    assert functions.Benefit(sum, price, arrdata) == (47.5, 0.0)

    #Test case: one line of data, sum is bigger than arrline[0]
    arrdata = []
    arrline = functions.Record()
    arrline.quantity = '10.0'
    arrline.data = '1234567890'
    arrline.price = '5'
    arrdata.append(arrline)
    assert functions.Benefit(15, 10, arrdata) == False

    #Test case: one line without tax and one with
    arrdata = []
    arrline = functions.Record()
    arrline2 = functions.Record()
    arrline.quantity = '10.0'
    arrline.data = '1234567890'
    arrline.price = '0.5'
    arrdata.append(arrline)
    arrline2.quantity = '20.0'
    arrline2.data = str(time.time() - 1.0)
    arrline2.price = '1'
    arrdata.append(arrline2)

    assert functions.Benefit(15, 10, arrdata) == (140.0, 50.0)

    #Test case: without tax
    arrdata = []
    arrline3 = functions.Record()
    arrline4 = functions.Record()
    arrline3.quantity = '10.0'
    arrline3.data = '1234567890'
    arrline3.price = '50'
    arrdata.append(arrline3)
    arrline4.quantity = '20.0'
    arrline4.data = '1456748973'
    arrline4.price = '100'
    arrdata.append(arrline4)

    assert functions.Benefit(30, 80, arrdata) == (-100.0, 0.0)



# Run the test
pytest.main()
