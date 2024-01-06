import json
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from inventory.models import Category,Product,ProductImage,ProductReview




@api_view(['GET','POST'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def category(request):
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
    elif request.method == 'POST':
        category_name = request.data.get('category_name',None)
        if category_name:
            try:
                category_query = Category.objects.get(name=category_name)
                reponse_data = {
                    'message' : 'Category already exists',
                    'error' : True
                }
                return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
            except Category.DoesNotExist:
                category_query = Category.objects.create(name=category_name)
                reponse_data = {
                    'data' : {
                        'id' : category_query.id,
                        'name' : category_query.name,
                    }
                }
                return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
        else:
            reponse_data = {
                    'message' : 'invalid category_name',
                    'error' : True
                }
            return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')


@api_view(['GET'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def categories(request):
    categories_query = Category.objects.all()
    reponse_data = {
        'data' : [{
            'category_id' : category.id,
            'category_name' : category.name
        } for category in categories_query]
                }
    return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')


@api_view(['GET'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def products(request):
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
    
    
    
@api_view(['GET','POST'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def product(request):
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
    elif request.method == 'POST':
        product_name = request.data.get('product_name',None)
        product_image = request.data.get('product_image',None)
        product_description = request.data.get('product_description',None)
        product_price = request.data.get('product_price',None)
        product_stock = request.data.get('product_stock',None)
        category_id = request.data.get('category_id',None)
        if product_name and product_description and product_price and product_stock and category_id:
            product_query = Product.objects.create(
                name=product_name,
                description=product_description,
                price=product_price,
                stock=product_stock,
                category_id=category_id
            )
            if product_image:
                product_image_query = ProductImage.objects.create(
                    product=product_query,
                    image=product_image
                )
                product_image_query.save()
            reponse_data = {
                'data' : {
                    'product_id' : product_query.id,
                    'product_name' : product_query.name,
                    'product_description' : product_query.description,
                    'product_price' : product_query.price,
                    'product_stock' : product_query.stock,
                    'category_id' : product_query.category_id,
                    'product_image' : product_image_query.image.url,
                                        'product_images' : [
                            {
                                'product_image_id' : product_image.id,
                                'product_image' : product_image.image.url
                            } for product_image in ProductImage.objects.filter(product_id=product_query.id)
                        ]
                }
            }
            return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
        else:
            reponse_data = {
                    'message' : 'please make sure to send all parameters',
                    'error' : True
                }
            return Response(reponse_data, status=status.HTTP_200_OK, content_type='application/json')
        
        
        
