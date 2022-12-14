import pytest
from fixtures.fixtures import smtp_connection

@pytest.mark.integration
class TestSMTP(object):

  def test_ehlo(self, smtp_connection):
      response, msg = smtp_connection.ehlo()
      # this console output will only be shown if the test fails
      print("received message:" + str(msg))
      assert response == 250

  def test_noop(self, smtp_connection):
      response, msg = smtp_connection.noop()
      assert response == 250