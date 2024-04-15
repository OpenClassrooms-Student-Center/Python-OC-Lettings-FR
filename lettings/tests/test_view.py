import pytest
from unittest.mock import patch
from lettings.models import Letting
from lettings.views import LettingsViews

from unittest.mock import call


class TestIndex:

    @patch('lettings.views.render')
    def test_lettings_list_variable_is_empty(self, mock_render):
        # Arrange
        with patch('lettings.views.Letting.objects.all', return_value=[]):
            # Act
            LettingsViews.index(self)

            # Assert
            mock_render.assert_called_once_with(self, 'lettings/index.html', {'lettings_list': []})


class TestLetting:

    @patch('lettings.views.Letting.objects.get', side_effect=Letting.DoesNotExist)
    def test_raises_does_not_exist_exception_if_letting_does_not_exist(self, mock_get):
        # Arrange
        letting_id = 1

        # Act & Assert
        with pytest.raises(Letting.DoesNotExist):
            LettingsViews().letting(letting_id)

    @patch('lettings.views.Letting.objects.get', side_effect=Letting.MultipleObjectsReturned)
    def test_raises_multiple_objects_returned_exception_if_multiple_lettings_exist(self):
        # Arrange
        letting_id = 1

        # Act & Assert
        with pytest.raises(Letting.MultipleObjectsReturned):
            LettingsViews().letting(letting_id)

    @patch('lettings.views.Letting.objects.get')
    @patch('lettings.views.render')
    def test_raises_multiple_objects_returned_exception_if_multiple_lettings_exist(self, mock_render, mock_get):
        # Arrange
        letting_id = 1
        mock_get.side_effect = Letting.MultipleObjectsReturned

        # Act & Assert
        with pytest.raises(Letting.MultipleObjectsReturned):
            LettingsViews().letting(letting_id)

        # Assert
        mock_get.assert_called_once_with(id=letting_id)
        assert not mock_render.called
