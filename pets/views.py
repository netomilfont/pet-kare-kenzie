from rest_framework.views import APIView, Request, Response, status
from .models import Pet
from groups.models import Group
from traits.models import Trait
from .serializers import PetSerializer
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

class PetView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()

        result_page = self.paginate_queryset(pets, request, view=self)

        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group")
        trait_list = serializer.validated_data.pop("traits")

        group_obj = Group.objects.filter(scientific_name__iexact=group_data["scientific_name"]).first()

        if not group_obj:
            group_obj = Group.objects.create(**group_data)
        
        pet_obj = Pet.objects.create(**serializer.validated_data, group=group_obj)

        for trait_dict in trait_list:
            trait_obj = Trait.objects.filter(name__iexact=trait_dict["name"]).first()

            if not trait_obj:
                trait_obj = Trait.objects.create(**trait_dict)

            pet_obj.traits.add(trait_obj)

        serializer_return = PetSerializer(pet_obj)

        return Response(serializer_return.data, status.HTTP_201_CREATED)


class PetDetailView(APIView):
    def get(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pet)

        return Response(serializer.data)


    def patch(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        group_data:dict = serializer.validated_data.pop("group", None)
        trait_list:list = serializer.validated_data.pop("traits", None)

        if group_data:
            group_obj = Group.objects.filter(scientific_name__iexact=group_data["scientific_name"]).first()
            
            if not group_obj:
                group_obj:dict = Group.objects.create(**group_data)
                pet.group.add(group_obj)

            for key, value in group_data.items():
                setattr(pet.group, key, value)
            pet.group.save()

        if trait_list:
            for trait_dict in trait_list:
                trait_obj:dict = Trait.objects.filter(name__iexact=trait_dict["name"]).first()

                if not trait_obj:
                    trait_obj = Trait.objects.create(**trait_dict)
                    pet.traits.add(trait_obj)

                for key, value in trait_dict.items():
                    setattr(pet.traits, key, value)
                pet.traits.add()

        for key, value in serializer.validated_data.items():
            setattr(pet, key, value)

        pet.save()
        serializer_return = PetSerializer(pet)

        return Response(serializer_return.data, status.HTTP_200_OK)


    def delete(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)