from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SortRequestSerializer,SortResponseSerializer
from .sorting_alogrithm import bubble,selection,insertion,merge_sort


# Create your views here.
@api_view(['POST'])
def sort_array(request,algorithm):
     serializer = SortRequestSerializer(data=request.data)
     if serializer.is_valid():
        arr = serializer.validated_data['array']
        algorithm = serializer.validated_data['algorithm']

        if algorithm == 'bubble':
            sorted_array = bubble(arr)
        elif algorithm == 'selection':
            sorted_array = selection(arr)
        elif algorithm == 'insertion':
            sorted_array = insertion(arr)
        elif algorithm == 'merge':
            sorted_array = merge_sort(arr)
        
        response_data = {'sorted_array': sorted_array}
        response_serializer = SortResponseSerializer(response_data)

        return Response(response_serializer.data, status=status.HTTP_200_OK)

     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
                                                               



