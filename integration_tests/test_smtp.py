import pytest
from fixtures.fixtures import smtp_connection

@pytest.mark.integration
class TestSMTP(object):

  def test_ehlo(self, smtp_connection):
      response, msg = smtp_connection.ehlo()
      assert response == 250
      assert b"smtp.gmail.com" in msg

  def test_noop(self, smtp_connection):
      response, msg = smtp_connection.noop()
      assert response == 250