import pytest
 
@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    page.goto('http://localhost:8000')
    assert page.inner_text('h1') == 'Hello World'
 
@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    page.wait_for_function("document.getElementById('result').innerText.includes('Calculation Result')")
    assert page.inner_text('#result') == 'Calculation Result: 15'
 
@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '3')
    page.click('button:text("Subtract")')
    page.wait_for_function("document.getElementById('result').innerText.includes('Calculation Result')")
    assert page.inner_text('#result') == 'Calculation Result: 7'
 
@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '4')
    page.fill('#b', '5')
    page.click('button:text("Multiply")')
    page.wait_for_function("document.getElementById('result').innerText.includes('Calculation Result')")
    assert page.inner_text('#result') == 'Calculation Result: 20'
 
@pytest.mark.e2e
def test_calculator_divide(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '2')
    page.click('button:text("Divide")')
    page.wait_for_function("document.getElementById('result').innerText.includes('Calculation Result')")
    assert page.inner_text('#result') == 'Calculation Result: 5'
 
@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')
    page.wait_for_function("document.getElementById('result').innerText.includes('Error')")
    assert 'Error' in page.inner_text('#result')