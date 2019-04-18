from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Partner, Project
from django.core.serializers import serialize
from django.http import JsonResponse
from easy_thumbnails.files import get_thumbnailer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at geoslab app.")

def projects(request):

	fc = {"type":"FeatureCollection", "features": []}
	projects = Project.objects.all().order_by('name')
	projectsJson = []
	for p in projects:
		f = {"type": "Feature", "geometry": {"type": "Point", "coordinates": p.point.coords}, "properties": {"name": p.name, "description": p.description, "url_images": []}}
		# d = dict()
		# d['name'] = p.name
		# d['description'] = p.description
		# d['point'] = p.point.coords
		url_images = []
		if p.image1 != None:
			# url_images.append(p.image1.url)
			# thum = generate_Thumbnail(p.image1.original_filename, p.image1.url)
			# thum1 = 
			url_images.append({"image": p.image1.url, "thumbnail": generate_Thumbnail(p.image1.original_filename, p.image1).url})
		if p.image2 != None:
			# url_images.append(p.image2.url)
			url_images.append({"image": p.image2.url, "thumbnail": generate_Thumbnail(p.image2.original_filename, p.image2).url})
		if p.image3 != None:
			# url_images.append(p.image3.url)
			url_images.append({"image": p.image3.url, "thumbnail": generate_Thumbnail(p.image3.original_filename, p.image3).url})
		if p.image4 != None:
			# url_images.append(p.image4.url)
			url_images.append({"image": p.image4.url, "thumbnail": generate_Thumbnail(p.image4.original_filename, p.image4).url})
		if p.image5 != None:
			# url_images.append(p.image5.url)
			url_images.append({"image": p.image5.url, "thumbnail": generate_Thumbnail(p.image5.original_filename, p.image5).url})
		if p.image6 != None:
			# url_images.append(p.image6.url)
			url_images.append({"image": p.image6.url, "thumbnail": generate_Thumbnail(p.image6.original_filename, p.image6).url})
		if p.image7 != None:
			# url_images.append(p.image7.url)
			url_images.append({"image": p.image7.url, "thumbnail": generate_Thumbnail(p.image7.original_filename, p.image7).url})
		if p.image8 != None:
			# url_images.append(p.image8.url)
			url_images.append({"image": p.image8.url, "thumbnail": generate_Thumbnail(p.image8.original_filename, p.image8).url})
		if p.image9 != None:
			# url_images.append(p.image9.url)
			url_images.append({"image": p.image9.url, "thumbnail": generate_Thumbnail(p.image9.original_filename, p.image9).url})
		if p.image10 != None:
			# url_images.append(p.image10.url)
			url_images.append({"image": p.image10.url, "thumbnail": generate_Thumbnail(p.image10.original_filename, p.image10).url})

		if len(url_images) > 0:
			f['properties']['url_images'] = url_images
		# d['images'] = url_images
		# projectsJson.append(d)
		fc['features'].append(f)
	return JsonResponse(fc, safe=False)

	# return HttpResponse(projects[0].image1.url)
	# return HttpResponse(serialize('json', Project.objects.all(), fields=('name', 'description', 'point', 'image1.url', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10')))

def generate_Thumbnail(name, image):
	# picture = open(url_img)
	thumbnailer = get_thumbnailer(image, relative_name=name)
	return thumbnailer.get_thumbnail({'size': (100, 100)})

class PartnerListView(ListView):
    template_name = 'partner_list.html'
    context_object_name = 'partner_list'

    def get_queryset(self):
        return Partner.objects.all()



# class ProjectViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     projects = Project.objects.all().order_by('name')
#     