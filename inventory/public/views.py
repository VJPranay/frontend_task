import json
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from inventory.models import Category,Product,ProductImage,ProductReview




@api_view(['GET'])
def pcategory(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id',None)
        if category_id:
            try:
                category_query = Category.objects.get(id=category_id)
                reponse_data = {
                    'data' : {
                        'category_id' : category_query.id,
                        'category_name' : category_query.name,
                               }
                }
                return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
            except Category.DoesNotExist:
                reponse_data = {
                    'message' : 'Category does not exist',
                    'error' : True
                }
                return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
        else:
            reponse_data = {
                    'message' : 'Category does not exist',
                    'error' : True
                }
            return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
    

@api_view(['GET'])
def pcategories(request):
    categories_query = Category.objects.all()
    reponse_data = {
        'data' : [{
            'category_id' : category.id,
            'category_name' : category.name
        } for category in categories_query]
                }
    return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')


@api_view(['GET'])
def pproducts(request):
    category_id = request.GET.get('category_id',None)
    if category_id:
        products_query = Product.objects.filter(
            category_id=category_id
        )
        reponse_data = {
            'data' : [
                {
                    'product_id' : product.id,
                    'product_name' : product.name,
                    'product_description' : product.description,
                    'product_price' : product.price,
                    'product_stock' : product.stock,
                    'category_id' : product.category_id,
                    'product_images' : [
                            {
                                'product_image_id' : product_image.id,
                                'product_image' : product_image.image.url
                            } for product_image in ProductImage.objects.filter(product_id=product.id)
                        ]
                    
                } for product in products_query
            ]
            }
        return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
    else:
        products_query = Product.objects.all()
        reponse_data = {
            'data' : [
                {
                    'product_id' : product.id,
                    'product_name' : product.name,
                    'product_description' : product.description,
                    'product_price' : product.price,
                    'product_stock' : product.stock,
                    'category_id' : product.category_id,
                        'product_images' : [
                            {
                                'product_image_id' : product_image.id,
                                'product_image' : product_image.image.url
                            } for product_image in ProductImage.objects.filter(product_id=product.id)
                        ]
                    
                } for product in products_query
            ]
            }
        return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
    
    
    
@api_view(['GET'])
def pproduct(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id',None)
        if product_id:
            try:
                product_query = Product.objects.get(id=product_id)
                reponse_data = {
                    'data' : {
                        'product_id' : product_query.id,
                        'product_name' : product_query.name,
                        'product_description' : product_query.description,
                        'product_price' : product_query.price,
                        'product_stock' : product_query.stock,
                        'category_id' : product_query.category_id,
                        'product_images' : [
                            {
                                'product_image_id' : product_image.id,
                                'product_image' : product_image.image.url
                            } for product_image in ProductImage.objects.filter(product_id=product_query.id)
                        ]
                    }
                }
                return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
            except Product.DoesNotExist:
                reponse_data = {
                    'message' : 'Product does not exist',
                    'error' : True
                }
                return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
        else:
            reponse_data = {
                    'message' : 'invalid product_id',
                    'error' : True
                }
            return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
        
        
        
