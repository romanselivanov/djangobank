from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import DnaSerializer
from rest_framework import status

class GetRoot(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DnaSerializer

    def get(self, request, format=None):
        return Response("Hello world", status=status.HTTP_200_OK)

    def post(self, request, format=None):       
        dna = ("tgacccactaatcagcaacatagcactttgagcaaaggcctgtgttggagctattggccc"
                "caaaactgcctttccctaaacagtgttcaccattgtagacctcaccactgttcgcgtaac"
                "aactggcatgtcctgggggttaatactcac")

        serializer = DnaSerializer(data=request.data)
        if serializer.is_valid():
            userinput = str(request.data["dna"]).lower()
            if not all(c.isalpha() for c in userinput):
                return Response("DNA sequence contains only letters", status=status.HTTP_200_OK)

            kodons = [dna[i:i+3] for i in range(0, len(dna), 3)]
            # вариант поиска 1
            if userinput in kodons:
                return Response("DNA sequence found", status=status.HTTP_200_OK)                          
            else:                    
                return Response("DNA sequence not found", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
