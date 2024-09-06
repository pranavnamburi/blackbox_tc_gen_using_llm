from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from openai import OpenAI
import boto3





client = OpenAI(
  api_key="sk-None-OoucK5PYM9opQRytgDnMT3BlbkFJR6n4PwWCEii8Xf2kh7zH", 
)

def default_view(request):
    return redirect(index)

def index(request):
    return render(request, 'index.html', context={})

def register_view(request):
    return redirect('/accounts/signup/')

def login_view(request):
    return redirect('/accounts/login/')

@login_required
def home_view(request):
    return render(request, 'home.html')

SYSTEM_CONTEXT = """ 
"Below are urls of images of a digital product's interface. Based on these images, please provide detailed testing procedures, identifying and describing. Each test case should contain the following:
test case ID,
test case description,
steps to follow,
expected results,
pass/fail criteria, and
status of the test case.
"""

@login_required
def file_upload_view(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        context = request.POST.get('context', '')

        if not files:
            messages.error(request, "Please upload at least one image.")
            return render(request, 'upload.html')

        
        def s3_url(ek_file):
            s3client= boto3.client('s3')
            bucket_name = 'myracle-bucket-upload'
            key = ek_file.name
            s3client.upload_fileobj(ek_file, bucket_name, key)
            url = f"https://{bucket_name}.s3.amazonaws.com/{key}"
            return url
        
       
        image_urls=[]
        for file in files:
            imager_url= s3_url(file)
            image_urls.append(imager_url)
        print(image_urls)
        
              
        user_content = [{"type": "text", "text": context}]
        user_content.extend([{"type": "image_url", "image_url": {"url": url}} for url in image_urls])
        

        
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                     {
                "role": "system",
                "content": SYSTEM_CONTEXT,
                    },
                    {
                        "role": "user",
                        "content": user_content,
                    }
                ],
            )
            result_text = response.choices[0].message.content.strip()
            
            return render(request, 'results.html', {'result_text': result_text})
        
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return render(request, 'upload.html')

    return render(request, 'upload.html')

def is_valid_file_type(filename):
    valid_extensions = ['.jpg', '.png', '.jpeg']
    return any(filename.endswith(ext) for ext in valid_extensions)

            
            
            