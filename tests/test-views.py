from django.test import TestCase,RequestFactory
from restaurant.views import MenuItemView
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory=RequestFactory()
        MenuItem.objects.create(
            title="Pasta",
            price=34.50,
            inventory=12
        )
        MenuItem.objects.create(
            title="Pizza",
            price=14.50,
            inventory=45
        )
    def test_getall(self):
        menuItems=MenuItem.objects.all()
        serialized_menuitems=MenuItemSerializer(menuItems,many=True)
        request=self.factory.get('restaurant/menu/')
        response=MenuItemView.as_view()(request)

        self.assertEqual(response.data,serialized_menuitems.data)