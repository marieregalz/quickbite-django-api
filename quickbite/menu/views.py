from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer


# ✅ CREATE + GET ALL + SEARCH + FILTER
class MenuList(APIView):
    def get(self, request):
        restaurant = request.GET.get("restaurant")
        category = request.GET.get("category")
        available = request.GET.get("available")

        menus = MenuItem.objects()

        # 🔍 Search by restaurant
        if restaurant:
            menus = menus.filter(restaurant_name=restaurant)

        # 🎯 Filter by category
        if category:
            menus = menus.filter(category=category)

        # 🎯 Filter by availability
        if available:
            if available.lower() == "true":
                menus = menus.filter(is_available=True)
            elif available.lower() == "false":
                menus = menus.filter(is_available=False)

        data = []
        for menu in menus:
            data.append({
                "id": str(menu.id),
                "restaurant_name": menu.restaurant_name,
                "menu_name": menu.menu_name,
                "category": menu.category,
                "price": menu.price,
                "spicy_level": menu.spicy_level,
                "is_available": menu.is_available,
                "description": menu.description,
                "created_at": menu.created_at,
            })

        return Response(data)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            menu = MenuItem(**serializer.validated_data)
            menu.save()
            return Response({"message": "Menu created successfully"})
        return Response(serializer.errors)


# ✅ GET BY ID + UPDATE + DELETE
class MenuDetail(APIView):
    def get(self, request, id):
        try:
            menu = MenuItem.objects.get(id=id)
            data = {
                "id": str(menu.id),
                "restaurant_name": menu.restaurant_name,
                "menu_name": menu.menu_name,
                "category": menu.category,
                "price": menu.price,
                "spicy_level": menu.spicy_level,
                "is_available": menu.is_available,
                "description": menu.description,
                "created_at": menu.created_at,
            }
            return Response(data)
        except:
            return Response({"error": "Menu not found"})

    def put(self, request, id):
        try:
            menu = MenuItem.objects.get(id=id)
            serializer = MenuItemSerializer(data=request.data)

            if serializer.is_valid():
                for key, value in serializer.validated_data.items():
                    setattr(menu, key, value)

                menu.save()
                return Response({"message": "Menu updated"})
            return Response(serializer.errors)
        except:
            return Response({"error": "Menu not found"})

    def delete(self, request, id):
        try:
            menu = MenuItem.objects.get(id=id)
            menu.delete()
            return Response({"message": "Menu deleted"})
        except:
            return Response({"error": "Menu not found"})