# from django.shortcuts import render
# from .models import MerchantAccount, MerchantAccountUser, MerchantAccountOwner
# from django.views import View
# from .forms import OrgForm

# class allMerchants(View):
#     template = 'merchants/merchantList.html'

#     form = OrgForm

#     def get(self, request):
#         context = {
#             'merchant_list': MerchantAccount.objects.all(),
#             'form': self.form(),
#         }

#         # def post(self, request):
#         # 	print(request.POST)
#         # 	form = self.form(request.POST)
#         # 	if form.is_valid():
#         # 		form.save()

#         # 		return redirect('blog:blog_home')

#         # 	else:
#         # 		context = {
#         # 			'form' : form,
#         # 			'merchant_list': MerchantProfile.objects.all()
#         # 		}
#         return render(request, self.template, context)

# class merchantSignup(View):
#     pass