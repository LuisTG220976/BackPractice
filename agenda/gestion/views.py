from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import PruebaSerializer, ImportanciaSerializer
from .models import Importancia



@api_view(http_method_names=['GET','POST'])
def endpointInicial(request: Request):
    print (request.method)
    if request.method =='GET':
        return Response(data={
            'message':'Bienvenido a mi API'
        }, status=200)

    elif request.method =='POST':
        return Response(data={
            'message':'Se creo la informacion correctamente'
        }, status=200)


class PruebaApiView(ListCreateAPIView):
    queryset = [
        {
            'id':1, 
            'nombre':'eduardo',
            'apellido':'de rivero'
        },
        {   
            'id':2,
            'nombre':'fiorella',
            'apellido':'marquez'
        }]
    serializer_class = PruebaSerializer 

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        validacion = data.is_valid()
        print(validacion)

        if validacion == True:
            print(data.validated_data)
            print(data.data)
            return Response(data={
                'message':'Prueba de creada exitosamente'
            }, status=201)  
        else:
            return Response(data={
                'message':'Error al crear la prueba',
                'content': data.errors
            },status=400)     


class ImportanciasView(ListCreateAPIView):
    queryset = Importancia.objects.all() #select * from importancia;
    serializer_class = ImportanciaSerializer