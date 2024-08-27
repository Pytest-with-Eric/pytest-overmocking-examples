import pytest
from unittest.mock import create_autospec


class PaymentProcessor:
    def process_payment(self, amount, currency="USD"):
        # Imagine this sends a payment request
        return True


@pytest.mark.xfail(reason="This test is expected to fail due to the extra argument")
def test_process_payment():
    mock_processor = create_autospec(PaymentProcessor)
    mock_processor.process_payment.return_value = True

    # This will now raise a TypeError if we attempt to call with incorrect arguments
    result = mock_processor.process_payment(100, "USD", "EXTRA_ARG")

    assert result is True
