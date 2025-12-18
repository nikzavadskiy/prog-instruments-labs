import pytest
from unittest.mock import patch, Mock
from src.payment import PaymentProcessor

class TestPayment:
    @patch('requests.get')
    def test_convert_price_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rate": 0.5}
        mock_get.return_value = mock_response

        processor = PaymentProcessor("http://fake.api")
        result = processor.convert_price(100, "USD")
        
        assert result == 50.0
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_convert_price_api_error(self, mock_get):
        mock_get.return_value.status_code = 500
        
        processor = PaymentProcessor("http://fake.api")
        with pytest.raises(Exception, match="API Error"):
            processor.convert_price(100, "USD")
